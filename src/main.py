import asyncio
from fastapi import FastAPI, HTTPException
from src.bootstrap.system_scanner import scan_system
from src.agents.watcher_agent import WatcherAgent
from src.agents.debt_scan_agent import DebtScanAgent
from src.agents.impact_score_agent import ImpactScoreAgent
from src.agents.refactor_plan_agent import RefactorPlanAgent
from src.agents.auto_patch_agent import AutoPatchAgent
from src.agents.pr_monitor_agent import PRMonitorAgent
from src.agents.velocity_track_agent import VelocityTrackAgent
from src.agents.learn_agent import LearnAgent
from src.payments.stripe_gate import StripeGate
from src.memory.debt_pattern_store import DebtPatternStore
from src.memory.velocity_graph import VelocityGraph
from src.memory.meta_learner import MetaLearner

app = FastAPI(title="Tech.Debt.Code", version="0.1.0")

@app.on_event("startup")
async def startup_event():
    # Scan system assets
    scan_system()
    
    # Initialize agents
    global watcher_agent, debt_scan_agent, impact_score_agent,
    refactor_plan_agent, auto_patch_agent, pr_monitor_agent,
    velocity_track_agent, learn_agent, stripe_gate,
    debt_pattern_store, velocity_graph, meta_learner
    
    watcher_agent = WatcherAgent()
    debt_scan_agent = DebtScanAgent()
    impact_score_agent = ImpactScoreAgent()
    refactor_plan_agent = RefactorPlanAgent()
    auto_patch_agent = AutoPatchAgent()
    pr_monitor_agent = PRMonitorAgent()
    velocity_track_agent = VelocityTrackAgent()
    learn_agent = LearnAgent()
    stripe_gate = StripeGate()
    debt_pattern_store = DebtPatternStore()
    velocity_graph = VelocityGraph()
    meta_learner = MetaLearner()

@app.get("/health")
async def health_check():
    return {
        "repos_tracked": 0,
        "patches_merged": 0,
        "avg_velocity_improvement": 0.0,
        "memory_hit_rate": 0.0
    }

@app.get("/api/system/profile")
async def get_system_profile():
    from src.bootstrap.system_profile import get_system_profile
    return get_system_profile()

@app.post("/api/debt/scan")
async def scan_debt(repo_url: str):
    try:
        result = await debt_scan_agent.scan_repo(repo_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/debt/{debt_id}/score")
async def get_debt_score(debt_id: str):
    try:
        score = debt_scan_agent.get_debt_score(debt_id)
        return score
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/debt/{debt_id}/refactors")
async def get_refactor_plan(debt_id: str):
    try:
        plan = refactor_plan_agent.generate_plan(debt_id)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/memory/patterns")
async def get_debt_patterns():
    try:
        patterns = debt_pattern_store.get_all_patterns()
        return patterns
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/payments/subscribe")
async def subscribe_payment(tier: str):
    try:
        result = stripe_gate.create_checkout_session(tier)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)