from github import *
import os, sys
from datetime import datetime

g = Github('abhinavchdhry', 'chmod777', user_agent='abhinavchdhry')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')

f = None
path = os.path.join('.', 'shalist')
if os.path.isfile(path):
	f = open('shalist', 'r')
else:
	print 'No shalist found.'
	sys.exit()

shas = []
for s in f:
	shas.append(s.strip('\n'))
#print shas
failed_shas = []

def get(repo, sha):
	try:
		CSF = open(sha+'.txt', 'w')
		commit = r.get_commit(sha)
		CSF.write('AUTHOR '+ commit.commit.author.name + '\n')
		CSF.write('DATE ' + datetime.isoformat(commit.commit.author.date) + '\n')
		fc = len(commit.files)
		CSF.write('FILECOUNT '+ str(fc) + '\n')
		for j in range(0,fc):
			CSF.write('FILENAME ' + commit.files[j].filename + '\n')
			CSF.write('ADD ' + str(commit.files[j].additions) + '\n')
			CSF.write('DEL ' + str(commit.files[j].deletions) + '\n')
			CSF.write('PATCH'+'\n')
			CSF.write(commit.files[j].patch)
			CSF.write('\n')
		CSF.close()
		print sha + '...successful.' + '\n'
		return 1
	except Exception:
		CSF.close()
		path = os.path.join('.', sha+'.txt')
		if os.path.isfile(path):
			os.unlink(path)
		print sha + '...failed.' + '\n'
		return 0

for i in range(0,len(shas)):
	failed_count = 0
	while get(r, shas[i])==0:
		failed_count += 1
		if failed_count >= 5:		
			failed_shas.append(shas[i])
			break

print 'Data for following commits could not be retrieved:'
for sha in failed_shas:
	print sha+'\n'
