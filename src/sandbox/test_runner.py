import subprocess
import os

def run_tests(repo_path):
    try:
        # Run test suite in sandboxed environment
        result = subprocess.run([
            "python", "-m", "pytest", "--tb=short"
        ], cwd=repo_path, capture_output=True, text=True)
        
        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "errors": result.stderr
        }
    except Exception as e:
        print(f"[ERROR] Test execution failed: {str(e)}")
        return {
            "success": False,
            "output": "",
            "errors": str(e)
        }