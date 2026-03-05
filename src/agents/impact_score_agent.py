import json
from src.memory.debt_pattern_store import DebtPatternStore
from src.memory.velocity_graph import VelocityGraph

class ImpactScoreAgent:
    def __init__(self):
        self.pattern_store = DebtPatternStore()
        self.velocity_graph = VelocityGraph()
    
    def score_debt_impact(self, debt_item):
        # Get similar patterns from memory
        similar_patterns = self.pattern_store.find_similar_patterns(debt_item)
        
        # Get velocity data
        velocity_data = self.velocity_graph.get_velocity_data(debt_item["file"])
        
        # Calculate impact score
        impact_score = 0.0
        velocity_impact = "low"
        roi_rank = 100
        safe_to_auto_patch = False
        estimated_effort_hours = 1.0
        memory_pattern_used = None
        
        if similar_patterns:
            # Weight by team-specific impact
            avg_impact = sum(p["velocity_correlation"] for p in similar_patterns) / len(similar_patterns)
            impact_score = avg_impact * debt_item.get("debt_score", 1.0)
            
            # Determine velocity impact level
            if impact_score > 0.8:
                velocity_impact = "high"
            elif impact_score > 0.5:
                velocity_impact = "medium"
            else:
                velocity_impact = "low"
            
            # Determine ROI rank (lower is better)
            roi_rank = int(100 - impact_score * 100)
            
            # Determine if safe to auto-patch
            if impact_score > 0.3 and debt_item.get("debt_score", 0) < 0.7:
                safe_to_auto_patch = True
            
            memory_pattern_used = similar_patterns[0]["pattern_type"]
        
        return {
            "debt_score": impact_score,
            "velocity_impact": velocity_impact,
            "roi_rank": roi_rank,
            "safe_to_auto_patch": safe_to_auto_patch,
            "estimated_effort_hours": estimated_effort_hours,
            "memory_pattern_used": memory_pattern_used
        }