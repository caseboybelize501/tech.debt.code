import subprocess
import json

class GoAnalyzer:
    def __init__(self):
        pass
    
    def run(self, repo_path):
        try:
            # Run golangci-lint on the repository
            result = subprocess.run([
                "golangci-lint", "run", "--out-format=json"
            ], cwd=repo_path, capture_output=True, text=True)
            
            findings = []
            if result.stdout:
                try:
                    data = json.loads(result.stdout)
                    for item in data:
                        findings.append({
                            "file": item["path"],
                            "line": item["line"],
                            "message": item["message"],
                            "severity": item["severity"]
                        })
                except Exception as e:
                    print(f"[ERROR] Failed to parse golangci-lint output: {str(e)}")
            
            return findings
        except Exception as e:
            print(f"[ERROR] Go analysis failed: {str(e)}")
            return []