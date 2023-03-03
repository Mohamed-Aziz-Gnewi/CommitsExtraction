import pandas as pd
from github import Github, UnknownObjectException, BadUserAgentException, BadAttributeException, RateLimitExceededException,BadCredentialsException, GithubException

myToken="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"

g=Github(myToken)

current_user = g.get_user()


repo = g.get_repo("PyGithub/PyGithub")

all_commits = repo.get_commits()

data = []
for commit in all_commits:   
    try:
        name = commit.author.name if commit.author is not None else 'NA'
    except AttributeError:
        name = 'NA'
        
    try:
        date = commit.author.created_at if commit.author is not None else 'NA'
    except AttributeError:
        date = 'NA'
        
    data.append({"name": name, "Date": date})

df_commits = pd.DataFrame(data, index=range(len(data)))
df_commits