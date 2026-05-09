class SupervisorAgent:

    def classify_task(self, user_goal):

        goal = user_goal.lower()

        if "research" in goal or "news" in goal:
            return "research"

        elif "pdf" in goal or "document" in goal:
            return "document"

        elif "schedule" in goal or "plan" in goal:
            return "productivity"

        elif "github" in goal or "repo" in goal:
            return "devops"

        return "general"

    def select_agents(self, workflow_type):

        mapping = {
            "research": ["research_agent"],
            "document": ["doc_agent"],
            "productivity": ["productivity_agent"],
            "devops": ["devops_agent"]
        }

        return mapping.get(workflow_type, [])

    def create_execution_plan(self, user_goal):

        workflow_type = self.classify_task(user_goal)

        agents = self.select_agents(workflow_type)

        execution_plan = {
            "goal": user_goal,
            "workflow_type": workflow_type,
            "agents": agents,
            "status": "planned"
        }

        return execution_plan


if __name__ == "__main__":

    supervisor = SupervisorAgent()

    sample_goal = "Research latest AI startups in India"

    plan = supervisor.create_execution_plan(sample_goal)

    print("\n===== EXECUTION PLAN =====")
    print(plan)