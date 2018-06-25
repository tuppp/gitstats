from github import Github

g1 = Github("luszuba","-0l6*#KP")

print('Organization Name')
org = g1.get_organization('tuppp')
print(org)

issues = org.get_issues()
for issue in issues:
	print(issue)

members = org.get_members()
members_list = []
for member in members:
	members_list.append(member)

has_in_members = org.has_in_members(members_list[0])
print (has_in_members)

public_members = org.get_public_members()
public_members_list = []
for public_member in public_members:
	public_members_list.append(public_member)

repos = org.get_repos()
repos_lsit=[]

print('\n\nRepos of the Organization')
for repo in repos:
    repos_lsit.append(repo)
    print(repo.name)
    

for r in org.get_repos():
    
    if r.name == 'leute':
        print('\n\nPrinting Commits for Leute Repository\n')
        for c in r.get_commits():
            print(c.commit.author.date,'\t\t',c.commit.author.name,'\t\t',c.commit.author.email)


print('\n\nTeam Members for the Organization')
teams = org.get_teams()
teams_list=[]
for team in teams:
    teams_list.append(team)
    for member in team.get_members():
        print(member.login)
