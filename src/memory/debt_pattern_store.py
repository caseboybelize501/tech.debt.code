import chromadb
from chromadb import Client
import json

class DebtPatternStore:
    def __init__(self):
        self.client = Client()
        self.collection = self.client.get_or_create_collection("debt_patterns")
    
    def add_pattern(self, pattern):
        # Add a new debt pattern to the store
        try:
            self.collection.add(
                documents=[json.dumps(pattern)],
                metadatas=[{
                    "pattern_type": pattern["pattern_type"],
                    "language": pattern["language"]
                }],
                ids=[f"pattern_{hash(str(pattern))}"]
            )
        except Exception as e:
            print(f"[ERROR] Failed to add pattern: {str(e)}")
    
    def find_similar_patterns(self, debt_item):
        # Find similar patterns in memory
        try:
            results = self.collection.query(
                query_texts=[json.dumps(debt_item)],
                n_results=5
            )
            
            return [json.loads(doc) for doc in results["documents"][0]]
        except Exception as e:
            print(f"[ERROR] Failed to find similar patterns: {str(e)}")
            return []
    
    def get_all_patterns(self):
        # Get all stored patterns
        try:
            results = self.collection.get()
            return [json.loads(doc) for doc in results["documents"]]
        except Exception as e:
            print(f"[ERROR] Failed to get all patterns: {str(e)}")
            return []