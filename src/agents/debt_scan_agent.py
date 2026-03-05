import os
import subprocess
import tempfile
from src.sandbox.runner import run_analysis
from src.analyzers.python_analyzer import PythonAnalyzer
from src.analyzers.javascript_analyzer import JavaScriptAnalyzer
from src.analyzers.go_analyzer import GoAnalyzer

class DebtScanAgent:
    def __init__(self):
        self.analyzers = {
            "python": PythonAnalyzer(),
            "javascript": JavaScriptAnalyzer(),
            "go": GoAnalyzer()
        }
    
    async def scan_repo(self, repo_url):
        # Clone to sandbox
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                subprocess.run(["git", "clone", repo_url, temp_dir], check=True)
                
                # Run static analysis
                results = self.run_static_analysis(temp_dir)
                
                # Git blame for ownership mapping
                ownership_map = self.git_blame_analysis(temp_dir)
                
                # Compute initial debt scores
                debt_scores = self.compute_debt_scores(results, ownership_map)
                
                return {
                    "repo_url": repo_url,
                    "debt_scores": debt_scores,
                    "analysis_results": results,
                    "ownership_map": ownership_map
                }
            except Exception as e:
                raise Exception(f"Debt scan failed: {str(e)}")
    
    def run_static_analysis(self, repo_path):
        # Run all available analyzers
        results = {}
        
        for lang, analyzer in self.analyzers.items():
            try:
                analysis_results = analyzer.run(repo_path)
                results[lang] = analysis_results
            except Exception as e:
                print(f"[ERROR] Failed to run {lang} analysis: {str(e)}")
        
        return results
    
    def git_blame_analysis(self, repo_path):
        # Simple implementation - in practice this would be more complex
        try:
            result = subprocess.run([
                "git", "blame", "--line-porcelain", "HEAD", "-p"
            ], cwd=repo_path, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print(f"[ERROR] Git blame failed: {str(e)}")
            return ""
    
    def compute_debt_scores(self, analysis_results, ownership_map):
        # Simple implementation - in practice this would be more complex
        scores = []
        
        for lang, results in analysis_results.items():
            for file_result in results:
                score = {
                    "file": file_result["file"],
                    "language": lang,
                    "debt_score": file_result.get("debt_score", 0.0),
                    "findings": file_result.get("findings", [])
                }
                scores.append(score)
        
        return scores
    
    def get_debt_score(self, debt_id):
        # Return specific debt score
        return {"id": debt_id, "score": 0.0}