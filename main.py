"""
Main script for the automated software development team.
This script orchestrates the collaboration between different agents to solve coding problems.
"""

import os
from dotenv import load_dotenv

# Load environment variables first, before other imports
load_dotenv()

import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler
import logging
import pytest
import sys
from io import StringIO
import re

from agents import create_agents

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("problem_solver")
console = Console()

def validate_environment():
    """Validate required environment variables."""
    required_vars = ['OPENAI_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            "Please check your .env file and ensure all required variables are set."
        )

def setup_directories():
    """Create necessary directories if they don't exist."""
    try:
        Path("problems/unsolved").mkdir(parents=True, exist_ok=True)
        Path("problems/solved").mkdir(parents=True, exist_ok=True)
        logger.info("Successfully created/verified required directories")
    except Exception as e:
        logger.error(f"Failed to create directories: {str(e)}")
        raise

def read_problem_file(file_path):
    """Read and return the contents of a problem file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                raise ValueError(f"Problem file {file_path} is empty")
            return content
    except Exception as e:
        logger.error(f"Failed to read problem file {file_path}: {str(e)}")
        raise

def run_tests(test_file):
    """Run pytest on the test file and return the results."""
    try:
        # Capture stdout to get test results
        stdout = StringIO()
        sys.stdout = stdout
        
        # Run pytest with clean output
        test_result = pytest.main([
            "-v",  # verbose output
            "--tb=short",  # shorter traceback format
            "--no-header",  # no header
            "--no-summary",  # no summary
            str(test_file)
        ])
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Get the captured output
        test_output = stdout.getvalue()
        
        # Clean up the output
        test_output = re.sub(r'=+ test session starts =+\n.*?\n', '', test_output, flags=re.DOTALL)
        test_output = re.sub(r'=+ warnings summary =+\n.*?\n', '', test_output, flags=re.DOTALL)
        test_output = re.sub(r'=+ short test summary info =+\n.*?\n', '', test_output, flags=re.DOTALL)
        test_output = test_output.strip()
        
        return {
            "success": test_result == pytest.ExitCode.OK,
            "output": test_output
        }
    except Exception as e:
        logger.error(f"Failed to run tests: {str(e)}")
        return {
            "success": False,
            "output": str(e)
        }

def save_solution(problem_name, analysis, code, tests):
    """Save the solution and related information to files."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        solution_dir = Path("problems/solved")
        
        # Create a module directory for the solution
        module_dir = solution_dir / f"{problem_name}_{timestamp}"
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Create an empty __init__.py to make it a package
        (module_dir / "__init__.py").touch()
        
        # Save code as a Python file
        code_file = module_dir / "solution.py"
        with open(code_file, 'w', encoding='utf-8') as f:
            f.write(code)
        
        # Save tests as a Python file
        test_file = module_dir / "test_solution.py"
        with open(test_file, 'w', encoding='utf-8') as f:
            # Write the test code with correct import
            f.write("import pytest\n")
            f.write("from .solution import *\n\n")
            f.write(tests)
        
        # Run the tests
        test_results = run_tests(test_file)
        
        # Save complete solution with test results
        solution_file = module_dir / "solution.json"
        solution_data = {
            "metadata": {
                "problem_name": problem_name,
                "timestamp": timestamp,
                "status": "PASSED" if test_results["success"] else "FAILED"
            },
            "problem": {
                "description": read_problem_file(Path("problems/unsolved") / f"{problem_name}.txt"),
                "analysis": analysis
            },
            "solution": {
                "code": code,
                "tests": tests
            },
            "test_results": {
                "success": test_results["success"],
                "output": test_results["output"]
            }
        }
        
        with open(solution_file, 'w', encoding='utf-8') as f:
            json.dump(solution_data, f, indent=2)
        
        logger.info(f"Solution saved to: {solution_file}")
        logger.info(f"Code saved to: {code_file}")
        logger.info(f"Tests saved to: {test_file}")
        logger.info(f"Test results: {'PASSED' if test_results['success'] else 'FAILED'}")
        if not test_results['success']:
            logger.info("Test output:")
            logger.info(test_results['output'])
        return solution_file
    except Exception as e:
        logger.error(f"Failed to save solution: {str(e)}")
        raise

def process_problem(problem_file):
    """Process a single problem file using the agent team."""
    try:
        problem_name = problem_file.stem
        problem_description = read_problem_file(problem_file)
        
        logger.info(f"Processing problem: {problem_name}")
        
        # Create agents
        agents = create_agents()
        
        # Step 1: Research Analyst analyzes the problem
        logger.info("Step 1: Analyzing problem...")
        analysis = agents['research_analyst'].analyze_problem(problem_description)
        logger.info("Analysis complete.")
        
        # Step 2: Python Developer implements the solution
        logger.info("Step 2: Implementing solution...")
        code = agents['python_developer'].implement_solution(analysis)
        logger.info("Implementation complete.")
        
        # Step 3: Test Engineer creates and runs tests
        logger.info("Step 3: Creating tests...")
        tests = agents['test_engineer'].create_tests(code)
        logger.info("Tests created.")
        
        # Save the solution
        solution_file = save_solution(
            problem_name,
            analysis,
            code,
            tests
        )
        
        logger.info(f"Successfully solved problem: {problem_name}")
        return solution_file
    except Exception as e:
        logger.error(f"Failed to process problem {problem_file}: {str(e)}")
        raise

def main():
    """Main entry point for the script."""
    try:
        # Validate environment and setup
        validate_environment()
        setup_directories()
        
        # Get all unsolved problems
        unsolved_dir = Path("problems/unsolved")
        problem_files = list(unsolved_dir.glob("*.txt"))
        
        if not problem_files:
            logger.info("No unsolved problems found.")
            return
        
        # Process each problem
        for problem_file in problem_files:
            try:
                process_problem(problem_file)
            except Exception as e:
                logger.error(f"Failed to process {problem_file}: {str(e)}")
                continue
        
    except Exception as e:
        logger.error(f"Script failed: {str(e)}")
        raise

if __name__ == "__main__":
    main() 