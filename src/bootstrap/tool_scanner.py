import subprocess
import json

def scan_tools():
    tools = []
    tool_names = ["pylint", "eslint", "golangci-lint", "rubocop"]
    
    for tool in tool_names:
        try:
            version_output = subprocess.check_output([tool, "--version"], text=True)
            path = subprocess.check_output(["which", tool], text=True).strip()
            tools.append({
                "name": tool,
                "version": version_output.strip(),
                "path": path
            })
        except Exception as e:
            print(f"[INFO] Tool {tool} not found: {str(e)}")
    
    return tools