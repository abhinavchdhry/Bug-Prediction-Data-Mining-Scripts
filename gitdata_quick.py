from github import *
from datetime import date
import os

start_date = date(2004, 6, 25)
end_date = date(2005, 6, 27)

filename = 'shalist'
path = os.path.join('.', filename)
if os.path.isfile(path):
	shas = []
	shalist = open(filename, 'r')
	for line in shalist.read():
		shas.append(line)
	shalist.close()
	shalist = open(filename, 'a')
else:
	shalist = open(filename, 'w')

g = Github('abhinavchdhry', 'chmod777', user_agent='abhinavchdhry')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')
c = r.get_commits()

last_commit_check = 0
running = 0
started = 0
count = 0

for commit in c:
	count += 1
	if count%1000 == 0:
		print count
	if running == 0:
		print 'Running...'
		running = 1
	current = commit.commit.author.date.date()
	if current >= start_date and current <= end_date:
		if started == 0:
			print 'Started...'
			started = 1
		if commit.sha not in shas:
			shalist.write(commit.sha)
			shalist.write('\n')
		last_commit_check = 1
	elif last_commit_check == 1:
		print 'End...'
		break
shalist.close()
