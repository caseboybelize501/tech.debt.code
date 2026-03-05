import json
import os

def write_system_profile(profile):
    with open("SystemProfile.json", "w") as f:
        json.dump(profile, f, indent=2)
    
    print(f"[INFO] System profile written to SystemProfile.json")

def get_system_profile():
    if not os.path.exists("SystemProfile.json"):
        raise Exception("SystemProfile.json not found. Run system scan first.")
    
    with open("SystemProfile.json", "r") as f:
        return json.load(f)