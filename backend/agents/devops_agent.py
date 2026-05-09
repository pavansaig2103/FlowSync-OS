from tools.groq_client import generate_ai_response


class DevOpsAgent:

    def execute(self, user_goal):

        print("\n[DevOps Agent] Handling infrastructure task...")

        prompt = f"""
You are a DevOps AI assistant.

Analyze the following task and provide:
1. Deployment strategy
2. Infrastructure suggestions
3. CI/CD pipeline steps
4. Possible risks

TASK:
{user_goal}
"""

        response = generate_ai_response(prompt)

        return {
            "agent": "devops_agent",
            "output": response,
            "type": "devops"
        }