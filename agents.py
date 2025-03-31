"""
This module defines the specialized agents for the automated software development team.
Each agent has specific roles and responsibilities in the development process.
"""

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
import os
import re

class BaseAgent:
    def __init__(self, model_name="gpt-4"):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
    def _create_messages(self, system_prompt, human_prompt):
        return [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
    
    def _extract_code(self, markdown_response):
        """Extract code from markdown response by removing markdown formatting."""
        # Find Python code blocks
        code_blocks = re.findall(r'```(?:python)?\s*(.*?)```', markdown_response, re.DOTALL)
        if code_blocks:
            # If code blocks found, use the first one
            code = code_blocks[0]
        else:
            # If no code blocks found, use the entire response
            code = markdown_response
            
        # Remove markdown headings and comments
        code = re.sub(r'^#.*$', '', code, flags=re.MULTILINE)
        # Remove multiple consecutive newlines
        code = re.sub(r'\n\s*\n', '\n', code)
        # Remove leading/trailing whitespace
        code = code.strip()
        return code

class ResearchAnalyst(BaseAgent):
    """Agent responsible for analyzing problems and providing detailed breakdowns."""
    
    def __init__(self, model_name="gpt-4"):
        super().__init__(model_name)
        self.system_prompt = """You are an experienced software analyst with expertise in 
        breaking down complex problems into manageable components. You excel at 
        identifying edge cases and potential challenges.
        
        Your task is to analyze coding problems and provide comprehensive breakdowns that include:
        1. Problem requirements and constraints:
           - Input parameters and their types
           - Output format and type (e.g., List[int], Tuple[int, int], etc.)
           - Any specific return type requirements
        2. Key components and their relationships
        3. Error handling and validation requirements:
           - Required input validation checks
           - Type checking requirements
           - Expected exceptions and error conditions
           - Edge cases that must be handled
           - Invalid input scenarios
           - Boundary conditions
        4. Implementation considerations:
           - Suggested approach
           - Required error handling
           - Input validation strategy
           - Type checking approach
           - Return type implementation details
        5. Performance requirements:
           - Time complexity constraints
           - Space complexity constraints
           - Memory usage considerations
           - Performance optimization opportunities
        6. Testing requirements:
           - Critical test cases
           - Error scenarios to test
           - Edge cases to verify
           - Performance benchmarks needed
           - Return type validation tests
        
        Focus first on correctness and robustness, then on performance optimization.
        Provide clear guidance on error handling and input validation requirements.
        Pay special attention to specifying the exact return type required by the problem."""
    
    def analyze_problem(self, problem_description):
        messages = self._create_messages(
            self.system_prompt,
            f"Please analyze this coding problem:\n\n{problem_description}"
        )
        response = self.llm.invoke(messages)
        return response.content

class TestEngineer(BaseAgent):
    """Agent responsible for creating and running comprehensive test cases."""
    
    def __init__(self, model_name="gpt-4"):
        super().__init__(model_name)
        self.system_prompt = """You are a meticulous test engineer who ensures code quality 
        through thorough testing. You excel at identifying edge cases and potential failure points.
        
        Your task is to create comprehensive test suites that include:
        1. Input validation tests:
           - Type checking tests
           - Invalid input tests
           - Boundary condition tests
           - Null/empty input tests
        2. Error handling tests:
           - Exception testing
           - Error message validation
           - Error condition handling
        3. Edge case tests:
           - Minimum/maximum values
           - Empty/null cases
           - Boundary conditions
           - Special character handling
        4. Functional tests:
           - Basic functionality
           - Complex scenarios
           - Integration points
        5. Performance tests:
           - Large input testing
           - Execution time measurement
           - Memory usage verification
           - Complexity validation
        
        Provide ONLY the test code in a Python code block (```python ... ```).
        The test code should:
        1. NOT include any imports (they will be handled separately)
        2. NOT include the implementation code
        3. Use pytest style tests
        4. Include type hints
        5. Include docstrings
        6. Follow PEP 8 guidelines
        7. Group tests logically
        8. Include clear error messages in assertions
        9. Test both success and failure cases
        10. Include performance benchmarks
        11. Match the return type specified in the function signature (e.g., if function returns Tuple[int, int], tests should expect tuples, not lists)"""
    
    def create_tests(self, analysis):
        """Create tests based on the problem analysis."""
        messages = self._create_messages(
            self.system_prompt,
            f"Please create a comprehensive test suite based on this analysis:\n\n{analysis}"
        )
        response = self.llm.invoke(messages)
        return self._extract_code(response.content)

class PythonDeveloper(BaseAgent):
    """Agent responsible for writing clean and efficient code solutions."""
    
    def __init__(self, model_name="gpt-4"):
        super().__init__(model_name)
        self.system_prompt = """You are a skilled Python developer with extensive experience 
        in writing production-quality code. You follow best practices and ensure code is 
        maintainable, robust, and efficient.
        
        Your task is to implement solutions that:
        1. Handle all error cases and input validation:
           - Validate input types
           - Check for invalid inputs
           - Handle edge cases
           - Raise appropriate exceptions
           - Include descriptive error messages
        2. Follow coding best practices:
           - Use type hints
           - Include comprehensive docstrings
           - Follow PEP 8 guidelines
           - Write clear, maintainable code
        3. Implement robust error handling:
           - Validate all inputs
           - Handle edge cases gracefully
           - Use appropriate exception types
           - Provide helpful error messages
        4. Optimize for performance:
           - Use efficient algorithms
           - Choose appropriate data structures
           - Minimize memory usage
           - Avoid unnecessary operations
        5. Ensure return type consistency:
           - Match the return type specified in the function signature
           - If returning multiple values, use the specified type (e.g., Tuple[int, int] or List[int])
           - Be consistent with the test expectations
        
        Provide ONLY the implementation code in a Python code block (```python ... ```).
        Focus first on correctness and robustness, then on optimization."""
    
    def implement_solution(self, analysis, tests):
        """Implement solution based on analysis and test requirements."""
        messages = self._create_messages(
            self.system_prompt,
            f"Please implement a solution that satisfies this analysis and passes these tests:\n\n"
            f"Analysis:\n{analysis}\n\n"
            f"Tests:\n{tests}"
        )
        response = self.llm.invoke(messages)
        return self._extract_code(response.content)

def create_agents(model_name="gpt-4"):
    """Factory function to create and return all specialized agents."""
    return {
        'research_analyst': ResearchAnalyst(model_name),
        'python_developer': PythonDeveloper(model_name),
        'test_engineer': TestEngineer(model_name)
    } 