# Automated Problem Solving System

This project implements an automated system for creating, analyzing, and solving coding problems using a team of specialized AI agents. The system focuses on producing high-quality, well-tested solutions with comprehensive documentation and error handling.

## Features

- **Problem Analysis**: Detailed breakdown of problem requirements, constraints, and edge cases
- **Test-Driven Development**: Comprehensive test suites created before implementation
- **Robust Implementation**: Solutions with thorough error handling and input validation
- **Performance Optimization**: Focus on efficient algorithms and data structures
- **Documentation**: Detailed documentation for all components
- **Type Safety**: Type hints throughout the codebase
- **Code Organization**: Clear separation of concerns between agents and utilities
- **Problem Management**: Organized storage of problems and solutions
- **Automated Testing**: Comprehensive test suites with performance benchmarks

## Project Structure

```
.
├── agents.py           # Specialized AI agents for different tasks
├── problem_solver.py   # Problem management and workflow coordination
├── problems/          # Storage for problem descriptions and analysis
│   ├── solved/       # Successfully solved problems
│   └── unsolved/     # Problems waiting to be solved
```

## Problem Organization

### Problem Structure
Each problem is organized as follows:
```
problems/
├── solved/
│   └── problem_name/
│       ├── solution.py      # Implementation
│       ├── test_solution.py # Test suite
│       └── metadata.json    # Problem metadata
└── unsolved/
    └── problem_name.txt    # Problem description
```

### Solution Structure
Each solution includes:
- Implementation with type hints and docstrings
- Comprehensive test suite
- Performance benchmarks
- Metadata with problem information

## Agents

### Research Analyst
- Analyzes problems and provides detailed breakdowns
- Identifies requirements, constraints, and edge cases
- Specifies error handling and validation requirements
- Determines performance requirements
- Creates problem metadata

### Test Engineer
- Creates comprehensive test suites
- Covers input validation, error handling, and edge cases
- Implements performance tests
- Follows testing best practices
- Ensures test coverage

### Python Developer
- Implements robust solutions
- Handles all error cases and input validation
- Follows coding best practices
- Optimizes for performance
- Maintains code quality

## Usage

The system can be run using the command-line interface:

```bash
python main.py
```

This will:
1. Process any unsolved problems in the `problems/unsolved/` directory
2. Generate solutions with comprehensive test suites
3. Save the results in the `problems/solved/` directory

Each solution includes:
- Implementation file (`solution.py`)
- Test suite (`test_solution.py`)
- Problem metadata (`metadata.json`)

Example output:
```
Processing problem: find_subarray_sum
Generating solution...
Running tests...
Solution saved to: problems/solved/find_subarray_sum/
```

## Requirements

- Python 3.8+
- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- LangChain
- pytest (for running tests)
- typing-extensions (for enhanced type hints)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   # On Windows (PowerShell)
   $env:OPENAI_API_KEY='your-api-key-here'
   
   # On Unix/Linux/MacOS
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Development Workflow

1. **Problem Creation**
   - Create problem description in `problems/unsolved/`
   - Include requirements, constraints, and examples

2. **Problem Analysis**
   - Research Analyst analyzes requirements
   - Creates detailed breakdown and metadata

3. **Test Development**
   - Test Engineer creates comprehensive test suite
   - Includes edge cases and performance tests

4. **Implementation**
   - Python Developer implements solution
   - Follows best practices and optimizes performance

5. **Validation**
   - Run test suite
   - Verify performance requirements
   - Check documentation and type hints

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

