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
        1. Problem requirements and constraints
        2. Key components and their relationships
        3. Potential challenges and edge cases
        4. Suggested approach for implementation
        5. Time and space complexity requirements
        6. Performance optimization opportunities
        7. Memory usage considerations
        8. Algorithmic efficiency requirements
        9. Data structure selection criteria
        10. Potential bottlenecks and how to avoid them
        
        Focus on identifying performance-critical aspects and optimization opportunities."""
    
    def analyze_problem(self, problem_description):
        messages = self._create_messages(
            self.system_prompt,
            f"Please analyze this coding problem:\n\n{problem_description}"
        )
        response = self.llm.invoke(messages)
        return response.content

class PythonDeveloper(BaseAgent):
    """Agent responsible for writing clean and efficient code solutions."""
    
    def __init__(self, model_name="gpt-4"):
        super().__init__(model_name)
        self.system_prompt = """You are a skilled Python developer with extensive experience 
        in writing production-quality code. You follow best practices and ensure code is 
        maintainable and efficient.
        
        Your task is to implement solutions that:
        1. Follow Python best practices and PEP 8 guidelines
        2. Include comprehensive documentation
        3. Handle error cases appropriately
        4. Are efficient and maintainable
        5. Include type hints
        6. Include docstrings for all functions and classes
        7. Prioritize performance optimization:
           - Avoid creating unnecessary string copies
           - Use efficient data structures
           - Minimize memory allocations
           - Consider time and space complexity
           - Use in-place operations when possible
           - Avoid expensive operations (regex, string copies)
           - Use two-pointer techniques for string/array operations
           - Implement early returns for better performance
        8. Handle edge cases efficiently
        9. Use appropriate data structures for the problem
        10. Consider memory usage and garbage collection
        11. Implement efficient algorithms (O(n) or better when possible)
        12. Avoid redundant computations
        13. Use built-in functions when they're more efficient
        14. Consider cache locality and memory access patterns
        
        Provide ONLY the implementation code in a Python code block (```python ... ```).
        Focus on creating efficient, production-ready code that will pass performance tests."""
    
    def implement_solution(self, analysis):
        messages = self._create_messages(
            self.system_prompt,
            f"Please implement a solution based on this analysis:\n\n{analysis}"
        )
        response = self.llm.invoke(messages)
        return self._extract_code(response.content)

class TestEngineer(BaseAgent):
    """Agent responsible for creating and running comprehensive test cases."""
    
    def __init__(self, model_name="gpt-4"):
        super().__init__(model_name)
        self.system_prompt = """You are a meticulous test engineer who ensures code quality 
        through thorough testing. You excel at identifying edge cases and potential failure points.
        
        Your task is to create comprehensive test suites that include:
        1. Unit tests for individual components
        2. Integration tests for component interactions
        3. Edge case testing
        4. Error case testing
        5. Performance testing:
           - Test with large inputs
           - Measure execution time
           - Check memory usage
           - Verify time complexity
           - Test with various input sizes
           - Include stress tests
        6. Memory leak testing
        7. Concurrency testing (if applicable)
        8. Resource usage testing
        
        Provide ONLY the test code in a Python code block (```python ... ```).
        The test code should:
        1. NOT include any imports (they will be handled separately)
        2. NOT include the implementation code
        3. Use pytest style tests (no unittest)
        4. Include type hints where appropriate
        5. Include docstrings for test functions
        6. Follow PEP 8 guidelines
        7. Assume all necessary functions are already imported
        8. Use time.time() for performance testing
        9. Group related tests into separate functions
        10. Use descriptive test names that explain what is being tested
        11. Include clear comments explaining test cases
        12. Use pytest.raises for testing exceptions
        13. Include assertions with descriptive messages
        14. Test both successful and failure cases
        15. Include performance benchmarks
        16. Test with various input sizes
        17. Include stress tests for performance-critical functions"""
    
    def create_tests(self, code):
        messages = self._create_messages(
            self.system_prompt,
            f"Please create a comprehensive test suite for this code:\n\n{code}"
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