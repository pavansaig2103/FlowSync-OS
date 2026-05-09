class TaskPlanner:

    def create_plan(self, user_goal: str):

        goal = user_goal.lower()

        plan = {
            "workflow_type": "simple",
            "steps": [],
            "agents": []
        }

        # ---------------------------
        # 1. RESEARCH INTENT
        # ---------------------------
        if any(word in goal for word in ["research", "latest", "trend", "news"]):

            plan["steps"].append("Gather real-time information")
            plan["agents"].append("research_agent")

        # ---------------------------
        # 2. DOCUMENT / REPORT INTENT
        # ---------------------------
        if any(word in goal for word in ["report", "summarize", "write", "document"]):

            plan["steps"].append("Generate structured report")
            plan["agents"].append("doc_agent")

        # ---------------------------
        # 3. PRODUCTIVITY INTENT
        # ---------------------------
        if any(word in goal for word in ["plan", "schedule", "task", "organize"]):

            plan["steps"].append("Optimize productivity workflow")
            plan["agents"].append("productivity_agent")

        # ---------------------------
        # 4. DEVOPS INTENT
        # ---------------------------
        if any(word in goal for word in ["deploy", "docker", "server", "ci", "pipeline"]):

            plan["steps"].append("Handle devops automation")
            plan["agents"].append("devops_agent")

        # ---------------------------
        # DEFAULT FALLBACK
        # ---------------------------
        if not plan["agents"]:
            plan["steps"].append("General reasoning")
            plan["agents"].append("research_agent")

        return plan


# quick test
if __name__ == "__main__":

    planner = TaskPlanner()

    result = planner.create_plan(
        "Research latest AI startups and write a report"
    )

    print("\n===== TASK PLAN =====")
    print(result)