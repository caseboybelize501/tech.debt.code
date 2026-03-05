import asyncio
import time
from src.bootstrap.known_repos_store import KnownReposStore
from github import Github

class WatcherAgent:
    def __init__(self):
        self.known_repos = KnownReposStore()
        self.github = Github()
        
    async def poll_repos(self):
        while True:
            try:
                # Get repos from caseboybelize501
                user = self.github.get_user("caseboybelize501")
                repos = user.get_repos()
                
                current_repos = [repo.full_name for repo in repos]
                known_repos = self.known_repos.get_repos()
                
                new_repos = set(current_repos) - set(known_repos)
                
                if new_repos:
                    print(f"[INFO] Found {len(new_repos)} new repos")
                    for repo in new_repos:
                        self.known_repos.add_repo(repo)
                        # Queue for debt scan
                        await self.queue_debt_scan(repo)
                
                time.sleep(300)  # Poll every 5 minutes
            except Exception as e:
                print(f"[ERROR] Failed to poll repos: {str(e)}")
                time.sleep(60)
    
    async def queue_debt_scan(self, repo_url):
        # This would be implemented with Celery or similar
        print(f"[INFO] Queued debt scan for {repo_url}")