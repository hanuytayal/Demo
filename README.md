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

## Project Structure

```
.
├── agents.py           # Specialized AI agents for different tasks
├── problem_solver.py   # Problem management and workflow coordination
├── problems/          # Storage for problem descriptions and analysis
├── solutions/         # Implemented solutions
└── tests/            # Test suites for solutions
```

## Agents

### Research Analyst
- Analyzes problems and provides detailed breakdowns
- Identifies requirements, constraints, and edge cases
- Specifies error handling and validation requirements
- Determines performance requirements

### Test Engineer
- Creates comprehensive test suites
- Covers input validation, error handling, and edge cases
- Implements performance tests
- Follows testing best practices

### Python Developer
- Implements robust solutions
- Handles all error cases and input validation
- Follows coding best practices
- Optimizes for performance

## Usage

```python
from problem_solver import ProblemManager

# Initialize the problem manager
manager = ProblemManager()

# Create and solve a problem
problem_path, solution_path, test_path = manager.solve_problem(
    description="Implement a function that finds the longest palindrome in a string",
    difficulty="medium"
)

# Create a problem without solving
problem_id, problem_content = manager.create_problem(
    description="Find all prime numbers up to n using the Sieve of Eratosthenes",
    difficulty="hard"
)

# Implement a solution for an existing problem
solution_path, test_path = manager.implement_solution(problem_id, problem_content)
```

## Requirements

- Python 3.8+
- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- LangChain
- pytest (for running tests)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

