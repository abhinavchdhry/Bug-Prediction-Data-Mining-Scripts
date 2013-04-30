from github import *
import os, re
from datetime import date, timedelta

release_date = date(2005, 6, 27)
final_date = release_date + timedelta(days=365)
#final_date = date(2005, 6, 27)

g = Github('abhinavchdhry', 'chmod777', user_agent='abhinavchdhry')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')
print 'Acquired repo info...'

c = r.get_commits()
print 'Got commits...'

shas = []
start = False
count = 0
for commit in c:
	print count
	if count < 600:
		count += 1
		continue
	else:
		date = commit.commit.author.date.date()
		if date > release_date and date <= final_date:
			shas.append(commit.sha)
			print commit.sha
		count += 1
print shas
