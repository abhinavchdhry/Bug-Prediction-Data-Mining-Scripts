from github import *
import os, re

g = Github('abhinavchdhry', 'chmod777')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')

for f in os.listdir('.'):
	if f.endswith('.txt'):
		sha = f.strip('.txt')
#		m = r.get_commit(sha).commit.message
		fh = open(f, 'r')
		found = False
		for line in fh:
			if re.search('^MESSAGE\s', line):
				found = True
				break
		if not found:
			fh.close()
			fh = open(f, 'a')
			m = r.get_commit(sha).commit.message
			fh.write('MESSAGE '+ m)
			fh.write('\n')
			print sha + '...done'
			fh.close()
