from tools.groq_client import generate_ai_response
from tools.tavily_tool import search_web


class ResearchAgent:

    def execute(self, user_goal):

        web_results = search_web(user_goal)

        formatted_data = "\n".join(
            f"- {r['title']}: {r['content']}"
            for r in web_results
        )

        prompt = f"""
You are an advanced AI Research Agent.

Analyze the following live web research data and provide:

1. Key trends  
2. Important insights  
3. Risks/opportunities  
4. Future outlook  
5. Executive summary  

WEB DATA:
{formatted_data}
"""

        ai_response = generate_ai_response(prompt)

        return {
            "agent": "Research Agent",
            "task": user_goal,
            "web_data": web_results,
            "ai_response": ai_response,
            "status": "completed"
        }


if __name__ == "__main__":
    agent = ResearchAgent()
    response = agent.execute("Latest AI startup ecosystem in India")
    print(response)