from tools.groq_client import generate_ai_response


class DocAgent:

    def execute(self, user_goal, research_data=None):

        print("\n[Doc Agent] Creating structured document...")

        prompt = f"""
You are a professional technical document writer.

Convert the following information into a clean structured report.

USER GOAL:
{user_goal}

RESEARCH DATA:
{research_data}

FORMAT:
1. Title
2. Executive Summary
3. Detailed Analysis
4. Key Points
5. Conclusion
"""

        response = generate_ai_response(prompt)

        return {
            "agent": "doc_agent",
            "output": response,
            "type": "document"
        }