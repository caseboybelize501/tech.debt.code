import numpy as np
from sklearn.linear_model import LinearRegression
from src.memory.meta_learner import MetaLearner
from src.memory.debt_pattern_store import DebtPatternStore

class LearnAgent:
    def __init__(self):
        self.meta_learner = MetaLearner()
        self.pattern_store = DebtPatternStore()
    
    def learn_from_debt(self, debt_data):
        # Update meta-learning model with new data
        try:
            # Extract features from debt data
            features = self.extract_features(debt_data)
            
            # Update model
            self.meta_learner.partial_fit(features, debt_data["velocity_impact"])
            
            print("[INFO] Updated learning model with new debt data")
        except Exception as e:
            print(f"[ERROR] Failed to learn from debt: {str(e)}")
    
    def extract_features(self, debt_data):
        # Extract features for ML model
        return np.array([
            debt_data.get("debt_score", 0.0),
            debt_data.get("churn_rate", 0.0),
            debt_data.get("coverage_gap", 0.0),
            debt_data.get("complexity", 0.0)
        ])
    
    def get_recommended_approach(self, repo_type):
        # Query meta-learner for best approach
        return self.meta_learner.predict(repo_type)