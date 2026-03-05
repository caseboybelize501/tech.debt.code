import subprocess
import tempfile
import os

def run_analysis(repo_path, tools):
    results = {}
    
    for tool in tools:
        try:
            if tool == "pylint":
                result = subprocess.run([
                    "pylint", "--output-format=json", "--reports=n",
                    "--disable=C0111,C0103", "."
                ], cwd=repo_path, capture_output=True, text=True)
                results[tool] = result.stdout
            elif tool == "eslint":
                result = subprocess.run([
                    "eslint", "--format=json", "--max-warnings=0", "."
                ], cwd=repo_path, capture_output=True, text=True)
                results[tool] = result.stdout
            elif tool == "golangci-lint":
                result = subprocess.run([
                    "golangci-lint", "run", "--out-format=json"
                ], cwd=repo_path, capture_output=True, text=True)
                results[tool] = result.stdout
        except Exception as e:
            print(f"[ERROR] Failed to run {tool}: {str(e)}")
    
    return results