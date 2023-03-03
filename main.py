from github import Github
import pandas as pd

myToken="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"

g=Github(myToken)

current_user=g.get_user()
print(current_user.name)

repo = g.get_repo("Asabeneh/30-Days-Of-Python")
data=[]


all_commits=repo.get_commits()
for commit in all_commits:
     #Name elli aamal el commit w wakteh
     
    if commit.author is  None or commit.author.name == None:
        pass
    else:
        data.append((commit.author.name,commit.author.created_at))

df = pd.DataFrame(data, columns =['Name', 'created_at'])
print(df)

    

