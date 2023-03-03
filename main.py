from github import Github
import subprocess
import pandas as pd

myToken="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"

g=Github(myToken)

#current_user=g.get_user()
#print(current_user.name)

repo = g.get_repo("Mohamed-Aziz-Gnewi/CommitsExtraction")
# data=[]


commits=repo.get_commits()
# for commit in all_commits:
#      #Name elli aamal el commit w wakteh
     
#     if commit.author is  None or commit.author.name == None:
#         pass
#     else:
#         data.append((commit.author.name,commit.author.created_at))

# df = pd.DataFrame(data, columns =['Name', 'created_at'])
# print(df)
#last_commit = repo.get_commits(sha="master")[0]
#print(last_commit.commit.author.name)
branches = repo.get_branches()
#for branche in branches:
#    print(branche.name)
#branches = repo.get_branches()

for commit in commits:
    commit_sha = commit.sha
    # Get the Git tree object for the commit
    commit_tree = commit.commit.tree
    # Use the git command to get the branches that contain the commit
    command = f"git branch -a --contains {commit_sha}"
    output = subprocess.check_output(command.split(), cwd=repo.git_dir).decode()
    # Loop through each branch and print the branch name
    for branch in output.splitlines():
        print(f"Commit {commit_sha} was added on branch {branch.strip()}")

    

