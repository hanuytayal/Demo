# Automated Problem-Solving System Architecture

## Overview

This system implements an automated software development workflow using specialized AI agents to analyze, test, and solve coding problems. The system follows a modular architecture with clear separation of concerns between different components.

## Core Components

### 1. Main Script (`main.py`)

The main script orchestrates the entire workflow and provides the following functionality:

#### Environment Setup
- Validates required environment variables (OPENAI_API_KEY)
- Sets up necessary directory structure
- Configures logging with rich formatting

#### File Management
- Creates and manages directory structure:
  - `problems/unsolved/`: Contains problem descriptions
  - `problems/solved/`: Contains completed solutions
- Handles file I/O operations for problems and solutions

#### Test Runner
- Executes pytest-based test suites
- Captures and formats test output
- Provides test result analysis

#### Solution Management
- Creates timestamped solution directories
- Saves implementation code, tests, and metadata
- Maintains solution history

#### Workflow Orchestration
- Processes each unsolved problem sequentially
- Coordinates between different agents
- Handles errors and exceptions gracefully

### 2. Agent System (`agents.py`)

The agent system implements specialized AI agents using the LangChain framework and OpenAI's GPT-4 model.

#### Base Agent (`BaseAgent`)
Common functionality for all agents:
- LLM initialization and configuration
- Message formatting
- Code extraction from responses

#### Research Analyst (`ResearchAnalyst`)
Responsibilities:
- Problem analysis
- Requirements identification
- Edge case detection
- Performance considerations
- Error handling requirements

Analysis includes:
1. Problem requirements and constraints
2. Key components and relationships
3. Error handling and validation requirements
4. Implementation considerations
5. Performance requirements
6. Testing requirements

#### Test Engineer (`TestEngineer`)
Responsibilities:
- Test suite creation
- Edge case testing
- Performance testing
- Error handling verification

Test categories:
1. Input validation tests
2. Error handling tests
3. Edge case tests
4. Functional tests
5. Performance tests

#### Python Developer (`PythonDeveloper`)
Responsibilities:
- Solution implementation
- Code optimization
- Error handling
- Documentation

Implementation focus:
1. Input validation
2. Error handling
3. Code quality
4. Performance optimization

## Workflow

1. **Problem Discovery**
   - System scans `problems/unsolved/` directory
   - Identifies `.txt` files containing problem descriptions

2. **Problem Analysis**
   - Research Analyst agent analyzes problem
   - Generates comprehensive breakdown
   - Identifies requirements and constraints

3. **Test Creation**
   - Test Engineer agent creates test suite
   - Implements comprehensive test cases
   - Covers edge cases and performance

4. **Solution Implementation**
   - Python Developer agent implements solution
   - Follows best practices
   - Handles all error cases
   - Optimizes for performance

5. **Solution Validation**
   - Runs test suite
   - Verifies implementation
   - Checks performance requirements

6. **Solution Storage**
   - Creates timestamped solution directory
   - Saves all components:
     - Implementation (`solution.py`)
     - Tests (`test_solution.py`)
     - Metadata (`solution.json`)
     - Analysis and results

## Directory Structure

```
.
├── main.py                 # Main orchestration script
├── agents.py              # Agent implementations
├── problems/              # Problem storage
│   ├── unsolved/         # Unsolved problem descriptions
│   │   └── *.txt         # Problem files
│   └── solved/           # Completed solutions
│       └── problem_name_timestamp/  # Solution directories
│           ├── solution.py          # Implementation
│           ├── test_solution.py     # Tests
│           └── solution.json        # Metadata
├── .env                   # Environment variables
└── requirements.txt       # Dependencies
```

## Solution Format

Each solution is stored in a timestamped directory with:

### 1. Implementation (`solution.py`)
- Function implementation
- Type hints
- Docstrings
- Error handling

### 2. Tests (`test_solution.py`)
- Pytest test suite
- Input validation tests
- Edge case tests
- Performance tests

### 3. Metadata (`solution.json`)
```json
{
    "metadata": {
        "problem_name": "string",
        "timestamp": "YYYYMMDD_HHMMSS",
        "status": "PASSED|FAILED"
    },
    "problem": {
        "description": "string",
        "analysis": "string"
    },
    "solution": {
        "code": "string",
        "tests": "string"
    },
    "test_results": {
        "success": boolean,
        "output": "string"
    }
}
```

## Dependencies

- Python 3.8+
- OpenAI API key
- LangChain
- pytest
- rich (for logging)
- python-dotenv

## Error Handling

The system implements comprehensive error handling:

1. **Environment Errors**
   - Missing API keys
   - Invalid configurations

2. **File System Errors**
   - Missing directories
   - File access issues
   - Invalid file formats

3. **Agent Errors**
   - API failures
   - Invalid responses
   - Timeout issues

4. **Test Failures**
   - Failed assertions
   - Performance issues
   - Implementation errors

## Best Practices

1. **Code Quality**
   - Type hints throughout
   - Comprehensive docstrings
   - PEP 8 compliance
   - Clear error messages

2. **Testing**
   - Comprehensive test coverage
   - Edge case handling
   - Performance validation
   - Clear test documentation

3. **Error Handling**
   - Graceful error recovery
   - Detailed error messages
   - Proper exception types
   - Input validation

4. **Documentation**
   - Clear code comments
   - Detailed docstrings
   - Architecture documentation
   - Usage examples 