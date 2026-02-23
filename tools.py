# tools.py
import math

def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

def web_search(query: str) -> str:
    # Mock tool for now
    return f"Search results for '{query}' (mocked result)"