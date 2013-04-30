from github import *
import re, os
from datetime import date, timedelta

g = Github('abhinavchdhry', 'chmod777')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')
print 'Repo info acquired...'

f = open('bug_shas.dat', 'r')
f1 = open('mldata_filtered', 'r')
f2 = open('final_bug_list.dat', 'w')

flist = []
for line in f1:
	flist.append(line.split(',')[0].strip('\s'))

bug_list = dict()
def get_message(r, sha):
	try:
		message = r.get_commit(sha).commit.message
		if re.search('Bug\s|bug\s|fix\s|Fix\s', message):
			print 'Match'
			filelist = r.get_commit(sha).files
			for x in filelist:
				fname = x.filename.split('/').pop().strip('\n')
				if fname in flist:
					if fname in bug_list:
						bug_list[fname] += 1
					else:
						bug_list[fname] = 1
		return 1
	except Exception:
		print 'Exception'
		return 0

for sha in f:
	print sha
	check = 0
	while get_message(r,sha.strip('\n')) == 0:
		check += 1
		if check > 5:
			print sha + ' failed.'
			break
		pass
	print 'Done'

for bug in bug_list:
	data = []
	data.append(bug)
	data.append(str(bug_list[bug]))
	f2.write(','.join(data))
	f2.write('\n')
