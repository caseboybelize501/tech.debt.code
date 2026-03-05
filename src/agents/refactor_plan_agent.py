import json

class RefactorPlanAgent:
    def __init__(self):
        pass
    
    def generate_plan(self, debt_id):
        # In practice, this would use LLM to generate a structured plan
        return {
            "priority": 1,
            "debt_item": debt_id,
            "estimated_effort_hours": 2.0,
            "velocity_impact_score": 0.85,
            "safe_to_auto_patch": True,
            "refactor_steps": [
                {
                    "step": 1,
                    "description": "Extract function",
                    "code_change": "function extract_function() { ... }"
                }
            ]
        }