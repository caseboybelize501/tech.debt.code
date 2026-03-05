import os
import hashlib

def scan_models(paths):
    model_extensions = [".gguf", ".safetensors", ".bin"]
    models = []
    
    for path in paths:
        if not os.path.exists(path):
            continue
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if any(file.endswith(ext) for ext in model_extensions):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, "rb") as f:
                            file_hash = hashlib.sha256(f.read()).hexdigest()
                        models.append({
                            "path": full_path,
                            "sha256": file_hash
                        })
                    except Exception as e:
                        print(f"[ERROR] Failed to read {full_path}: {str(e)}")
    
    return models