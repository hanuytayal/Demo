"""
This module provides utilities for managing the automated problem-solving workflow.
It coordinates the agents and handles file operations for problems and solutions.
"""

import os
import json
from datetime import datetime
from typing import Dict, Optional, Tuple
from agents import create_agents

class ProblemManager:
    """Manages the workflow of analyzing, implementing and testing coding problems."""
    
    def __init__(self, model_name: str = "gpt-4"):
        """
        Initialize the ProblemManager with required directories and agents.
        
        Args:
            model_name: The name of the language model to use for the agents
        """
        self.agents = create_agents(model_name)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.problems_dir = os.path.join(self.base_dir, "problems")
        self.solutions_dir = os.path.join(self.base_dir, "solutions")
        self.tests_dir = os.path.join(self.base_dir, "tests")
        
        # Create necessary directories if they don't exist
        for directory in [self.problems_dir, self.solutions_dir, self.tests_dir]:
            os.makedirs(directory, exist_ok=True)
    
    def _generate_problem_id(self) -> str:
        """Generate a unique problem ID based on timestamp."""
        return f"prob_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def _save_problem(self, problem_id: str, content: Dict) -> str:
        """
        Save problem details to a JSON file.
        
        Args:
            problem_id: Unique identifier for the problem
            content: Dictionary containing problem details
            
        Returns:
            Path to the saved problem file
        """
        file_path = os.path.join(self.problems_dir, f"{problem_id}.json")
        with open(file_path, 'w') as f:
            json.dump(content, f, indent=4)
        return file_path
    
    def _save_solution(self, problem_id: str, solution_code: str) -> str:
        """
        Save solution code to a Python file.
        
        Args:
            problem_id: Unique identifier for the problem
            solution_code: The implementation code
            
        Returns:
            Path to the saved solution file
        """
        file_path = os.path.join(self.solutions_dir, f"{problem_id}.py")
        with open(file_path, 'w') as f:
            f.write(solution_code)
        return file_path
    
    def _save_tests(self, problem_id: str, test_code: str) -> str:
        """
        Save test code to a Python file.
        
        Args:
            problem_id: Unique identifier for the problem
            test_code: The test implementation
            
        Returns:
            Path to the saved test file
        """
        file_path = os.path.join(self.tests_dir, f"test_{problem_id}.py")
        with open(file_path, 'w') as f:
            f.write(test_code)
        return file_path
    
    def create_problem(self, description: str, difficulty: str = "medium") -> Tuple[str, Dict]:
        """
        Create a new problem with analysis.
        
        Args:
            description: Problem description
            difficulty: Problem difficulty level
            
        Returns:
            Tuple of (problem_id, problem_details)
        """
        # Generate problem ID
        problem_id = self._generate_problem_id()
        
        # Get problem analysis
        analysis = self.agents['research_analyst'].analyze_problem(description)
        
        # Create problem content
        content = {
            "id": problem_id,
            "description": description,
            "difficulty": difficulty,
            "analysis": analysis,
            "created_at": datetime.now().isoformat()
        }
        
        # Save problem
        self._save_problem(problem_id, content)
        return problem_id, content
    
    def implement_solution(self, problem_id: str, problem_content: Dict) -> Tuple[str, str]:
        """
        Implement a solution for the given problem.
        
        Args:
            problem_id: Unique identifier for the problem
            problem_content: Dictionary containing problem details
            
        Returns:
            Tuple of (solution_path, test_path)
        """
        # Create tests first based on analysis
        test_code = self.agents['test_engineer'].create_tests(problem_content['analysis'])
        test_path = self._save_tests(problem_id, test_code)
        
        # Implement solution based on analysis and tests
        solution_code = self.agents['python_developer'].implement_solution(
            problem_content['analysis'],
            test_code
        )
        solution_path = self._save_solution(problem_id, solution_code)
        
        return solution_path, test_path
    
    def solve_problem(self, description: str, difficulty: str = "medium") -> Tuple[str, str, str]:
        """
        Complete workflow to create and solve a problem.
        
        Args:
            description: Problem description
            difficulty: Problem difficulty level
            
        Returns:
            Tuple of (problem_path, solution_path, test_path)
        """
        # Create problem
        problem_id, problem_content = self.create_problem(description, difficulty)
        problem_path = os.path.join(self.problems_dir, f"{problem_id}.json")
        
        # Implement solution
        solution_path, test_path = self.implement_solution(problem_id, problem_content)
        
        return problem_path, solution_path, test_path 