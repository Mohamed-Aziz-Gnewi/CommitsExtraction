from pydriller import Repository

# Replace with the URL of the GitHub repository you want to analyze
repo_url = "https://github.com/owner/repo.git"

# Replace with the local path where you want to clone the repository
repo_path = "/path/to/local/repo"

# Clone the repository using GitPython
from git import Repo
Repo.clone_from(repo_url, repo_path)

# Create a Repository object
repo = Repository(repo_path)

# Loop through each commit in the repository
for commit in repo.traverse_commits():
    # Get the branch name for the commit
    branch_name = commit.branches[0].name if commit.branches else "no branch"
    # Print the commit SHA and the branch name
    print(f"Commit {commit.hash} was added on branch {branch_name}")