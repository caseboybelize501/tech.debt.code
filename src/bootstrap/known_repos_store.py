import json
import os

class KnownReposStore:
    def __init__(self, filename="known_repos.json"):
        self.filename = filename
        if not os.path.exists(filename):
            self.repos = []
            self.save()
        else:
            with open(filename, "r") as f:
                self.repos = json.load(f)
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.repos, f, indent=2)
    
    def add_repo(self, repo_url):
        if repo_url not in self.repos:
            self.repos.append(repo_url)
            self.save()
    
    def get_repos(self):
        return self.repos
    
    def remove_repo(self, repo_url):
        if repo_url in self.repos:
            self.repos.remove(repo_url)
            self.save()