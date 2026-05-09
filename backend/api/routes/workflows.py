from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any, Optional
from core.orchestrator import Orchestrator

router = APIRouter()
orchestrator = Orchestrator()

class QueryRequest(BaseModel):
    query: str

@router.post("/run-workflow")
async def run_workflow(request: QueryRequest):
    try:
        # 1. Execute the actual multi-agent logic
        raw_result = orchestrator.execute_workflow(request.query)
        
        # 2. Extract and format results for "Bot-style" rendering
        # We ensure the 'results' field is a dictionary of findings
        findings = raw_result.get("results", {})
        if not findings and "result" in raw_result:
            # Fallback if the orchestrator returned a flat string
            findings = {"Analysis": raw_result["result"]}

        # 3. Construct the exact response the UI expects
        return {
            "status": "success",
            "output": {
                "agent_steps": raw_result.get("agent_steps", []),
                "trace_logs": raw_result.get("trace_logs", []),
                "result": {
                    "goal": request.query,
                    "workflow_type": raw_result.get("workflow_type", "Autonomous Research"),
                    "summary": "Deep-dive analysis complete. Strategic insights generated below.",
                    "results": findings
                }
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}