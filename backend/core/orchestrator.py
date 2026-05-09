from agents.supervisor import SupervisorAgent
from agents.research_agent import ResearchAgent
from core.task_planner import TaskPlanner
from core.retry_engine import RetryEngine
from datetime import datetime


class Orchestrator:

    def __init__(self):
        self.planner = TaskPlanner()
        self.retry_engine = RetryEngine()
        self.supervisor = SupervisorAgent()

        self.research_agent = ResearchAgent()

    def execute_workflow(self, user_goal):

        # -------------------------
        # STEP 1: CREATE PLAN
        # -------------------------
        plan = self.planner.create_plan(user_goal)

        print("\n===== EXECUTION PLAN =====")
        print(plan)

        results = []
        trace_logs = []

        trace_logs.append({
            "agent": "system",
            "level": "info",
            "message": "Workflow started",
            "timestamp": str(datetime.now())
        })

        # -------------------------
        # STEP 2: EXECUTE AGENTS
        # -------------------------
        for agent in plan["agents"]:

            trace_logs.append({
                "agent": agent,
                "level": "info",
                "message": f"Executing {agent}",
                "timestamp": str(datetime.now())
            })

            print(f"\n[ACTIVE AGENT]: {agent}")

            # -------------------------
            # RESEARCH AGENT
            # -------------------------
            if agent == "research_agent":

                result = self.retry_engine.run_with_retry(
                    self.research_agent.execute,
                    user_goal
                )

                results.append(result)

                trace_logs.append({
                    "agent": "research_agent",
                    "level": "success",
                    "message": "Research completed",
                    "timestamp": str(datetime.now())
                })

            # -------------------------
            # DOC AGENT (future)
            # -------------------------
            elif agent == "doc_agent":

                trace_logs.append({
                    "agent": "doc_agent",
                    "level": "warning",
                    "message": "Doc agent not implemented yet",
                    "timestamp": str(datetime.now())
                })

            # -------------------------
            # PRODUCTIVITY AGENT (future)
            # -------------------------
            elif agent == "productivity_agent":

                trace_logs.append({
                    "agent": "productivity_agent",
                    "level": "warning",
                    "message": "Productivity agent not implemented yet",
                    "timestamp": str(datetime.now())
                })

        # -------------------------
        # STEP 3: FINAL RESPONSE
        # -------------------------
        final_response = {
            "goal": user_goal,
            "workflow_type": plan.get("workflow_type", "sequential"),

            # 🔥 FRONTEND READY FIELDS
            "agent_steps": results,
            "trace_logs": trace_logs,

            "result": results[-1] if results else None,

            "status": "completed"
        }

        return final_response


# -------------------------
# TEST RUN
# -------------------------
if __name__ == "__main__":

    orchestrator = Orchestrator()

    response = orchestrator.execute_workflow(
        "Research latest AI startups in India"
    )

    print("\n===== FINAL RESPONSE =====")
    print(response)