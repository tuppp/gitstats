from github import Github
import numpy as np

authors = []
total = []
addition = []
deletion = []
comm = []

g1 = Github("luszuba","-0l6*#KP")

print('Organization Name')
org = g1.get_organization('tuppp')
print(org)

i = 0
count = 0
perc = 0
for r in org.get_repos():
        if r.name == "leute":
        continue
    print('\n\nAnalyzing Commits for '+r.name+' Repository\n')
    commits = r.get_commits()
    for x in commits:
        count +=1
    perc = 100/count
    for c in commits:
        author = c.commit.author.name
        tot = c.stats.total
        add = c.stats.additions
        delt = c.stats.deletions
        if author in authors:
            ind = authors.index(author)
            total[ind] += tot
            addition[ind] += add
            deletion[ind] += delt
            comm[ind] += 1

        else:
            authors.append(author)
            total.append(int(tot))
            addition.append(int(add))
            deletion.append(int(delt))
            comm.append(1)

        prc = float("%0.2f" % (perc*(i+1)))
        print(prc,'% Done')
        i += 1



print('There were total: ',len(authors),' committers . . .')
print('\nAvailable Commiters: ')
for n in authors:
    print(n)
choice = input('\n\n 1. Enter name of the committer for whom you want to see the statistic\n 2. Print stats for all users')
name = ''
if choice == '1':
    name = input("Enter name: ")

for n in authors:
    if n == name and choice == '1':
        ind = authors.index(n)
        print('\n\nLines of Code additions by ',n,' : ',addition[ind])
        print('Lines of Code deletions by ',n,' : ',deletion[ind])
        print('Total lines of Code contribution(add/del) by ',n,' : ',total[ind])
        print('Total commits : ',comm[ind])

    if choice == '2':
        ind = authors.index(n)
        print('\n\nLines of Code additions by ',n,' : ',addition[ind])
        print('Lines of Code deletions by ',n,' : ',deletion[ind])
        print('Total lines of Code contribution(add/del) by ',n,' : ',total[ind])
        print('Total commits : ',comm[ind])
    

