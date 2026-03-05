import subprocess
import json

class JavaScriptAnalyzer:
    def __init__(self):
        pass
    
    def run(self, repo_path):
        try:
            # Run eslint on the repository
            result = subprocess.run([
                "eslint", "--format=json", "--max-warnings=0", "."
            ], cwd=repo_path, capture_output=True, text=True)
            
            findings = []
            if result.stdout:
                try:
                    data = json.loads(result.stdout)
                    for item in data:
                        findings.append({
                            "file": item["filePath"],
                            "line": item["line"],
                            "message": item["message"],
                            "severity": item["severity"]
                        })
                except Exception as e:
                    print(f"[ERROR] Failed to parse eslint output: {str(e)}")
            
            return findings
        except Exception as e:
            print(f"[ERROR] JavaScript analysis failed: {str(e)}")
            return []