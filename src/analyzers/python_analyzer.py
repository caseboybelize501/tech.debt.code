import subprocess
import json

class PythonAnalyzer:
    def __init__(self):
        pass
    
    def run(self, repo_path):
        try:
            # Run pylint on the repository
            result = subprocess.run([
                "pylint", "--output-format=json", "--reports=n", "--disable=C0111,C0103",
                "--max-line-length=120", "."
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
                            "category": item["category"]
                        })
                except Exception as e:
                    print(f"[ERROR] Failed to parse pylint output: {str(e)}")
            
            return findings
        except Exception as e:
            print(f"[ERROR] Python analysis failed: {str(e)}")
            return []