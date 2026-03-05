from neo4j import GraphDatabase
import os

class VelocityGraph:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "password")
        
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def get_velocity_data(self, file_path):
        # Query velocity data for a specific file
        try:
            with self.driver.session() as session:
                result = session.run(
                    "MATCH (f:File {path: $file_path})-[:IMPACTS]->(v:VelocityDelta) RETURN v",
                    file_path=file_path
                )
                
                return [record["v"] for record in result]
        except Exception as e:
            print(f"[ERROR] Failed to get velocity data: {str(e)}")
            return []