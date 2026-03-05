from pydantic import BaseModel
from typing import List, Optional

class SystemProfile(BaseModel):
    model_files: List[dict]
    active_ports: List[int]
    tools: List[dict]
    git_version: str
    coverage_tools: List[str]

class DebtScore(BaseModel):
    file: str
    language: str
    debt_score: float
    findings: List[dict]


class RefactorPlanItem(BaseModel):
    priority: int
    debt_item: str
    estimated_effort_hours: float
    velocity_impact_score: float
    safe_to_auto_patch: bool
    refactor_steps: List[dict]


class AutoPatchResult(BaseModel):
    success: bool
    test_results: dict
    error: Optional[str] = None


class VelocityDelta(BaseModel):
    cycle_time_improvement: float
    test_failure_rate_delta: float
    velocity_impact_score: float