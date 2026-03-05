import os
import hashlib
import subprocess
import json
from src.bootstrap.model_scanner import scan_models
from src.bootstrap.tool_scanner import scan_tools
from src.bootstrap.port_registry import probe_ports
from src.bootstrap.system_profile import write_system_profile

def scan_system():
    print("[INFO] Starting system scan...")
    
    # Walk C:\ D:\ for model files
    model_files = scan_models(["C:\", "D:\"])
    
    # Probe inference servers
    active_ports = probe_ports()
    
    # Inventory static analysis tools
    tools = scan_tools()
    
    # Get git version
    try:
        git_version = subprocess.check_output(["git", "--version"], text=True).strip()
    except Exception as e:
        git_version = f"Error: {str(e)}"
    
    # Check coverage tools
    coverage_tools = []
    for tool in ["coverage", "c8", "gcov"]:
        try:
            subprocess.check_output([tool, "--version"], text=True)
            coverage_tools.append(tool)
        except Exception:
            pass
    
    # Create system profile
    system_profile = {
        "model_files": model_files,
        "active_ports": active_ports,
        "tools": tools,
        "git_version": git_version,
        "coverage_tools": coverage_tools
    }
    
    write_system_profile(system_profile)
    print("[INFO] System scan complete.")
    return system_profile