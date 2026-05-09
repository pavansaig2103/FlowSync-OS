from tools.groq_client import generate_ai_response


class ProductivityAgent:

    def execute(self, user_goal):

        print("\n[Productivity Agent] Optimizing workflow...")

        prompt = f"""
You are an AI productivity assistant.

Break down this task into actionable steps:

TASK:
{user_goal}

Provide:
1. Step-by-step plan
2. Time estimation
3. Priority order
4. Suggestions for efficiency
"""

        response = generate_ai_response(prompt)

        return {
            "agent": "productivity_agent",
            "output": response,
            "type": "plan"
        }