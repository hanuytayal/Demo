# Automated Problem-Solving System

This system uses AI agents to automatically analyze, implement, and test coding problems. It follows a structured workflow to ensure high-quality solutions with comprehensive test coverage.

## Features

- Automated problem analysis and breakdown
- Comprehensive test suite generation
- Clean and efficient code implementation
- Detailed solution documentation
- Test result validation and reporting

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. Place your problem descriptions in `problems/unsolved/` as `.txt` files.

2. Run the system:
   ```bash
   python main.py
   ```

3. The system will:
   - Analyze each problem
   - Generate test cases
   - Implement solutions
   - Run tests
   - Save results in `problems/solved/`

## Directory Structure

```
.
├── main.py                 # Main orchestration script
├── agents.py              # AI agent implementations
├── problems/              # Problem storage
│   ├── unsolved/         # Problem descriptions
│   └── solved/           # Completed solutions
├── .env                   # Environment variables
└── requirements.txt       # Dependencies
```

## Solution Format

Each solution is stored in a timestamped directory containing:
- `solution.py`: Implementation code
- `test_solution.py`: Test suite
- `solution.json`: Metadata and results

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in requirements.txt

## Documentation

For detailed system architecture and workflow, see [ARCHITECTURE.md](ARCHITECTURE.md).

