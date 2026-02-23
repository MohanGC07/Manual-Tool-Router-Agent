from groq import Groq
import os
from dotenv import load_dotenv
from tools import calculator, web_search

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TOOLS = {
    "calculator": calculator,
    "web_search": web_search,
}

class ToolAgent:

    def __init__(self, model="llama-3.3-70b-versatile"):
        self.model = model

    def call_llm(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    def route_tool(self, tool_name, tool_input):
        if tool_name in TOOLS:
            return TOOLS[tool_name](tool_input)
        return "Unknown tool"

    def run(self, goal):
        prompt = f"""
You are an intelligent agent.

Goal: {goal}

If a tool is needed, respond EXACTLY in this format:

TOOL: tool_name
INPUT: input_text

Available tools:
- calculator
- web_search

If no tool needed, provide final answer directly.
"""

        llm_output = self.call_llm(prompt)

        if "TOOL:" in llm_output:
            lines = llm_output.split("\n")
            tool_name = lines[0].replace("TOOL:", "").strip()
            tool_input = lines[1].replace("INPUT:", "").strip()

            tool_result = self.route_tool(tool_name, tool_input)

            final_prompt = f"""
Goal: {goal}

Tool used: {tool_name}
Tool result: {tool_result}

Now provide the final answer.
"""
            return self.call_llm(final_prompt)

        return llm_output