from github import *
import re, os, urllib
from datetime import date, timedelta

g = Github('abhinavchdhry', 'chmod777', user_agent='abhinavchdhry')
r = g.get_organization('eclipse').get_repo('eclipse.jdt.core')
print 'Repo info acquired...'

reldate = date(2005, 6, 27)
fdate = reldate + timedelta(days=180)
url = "https://bugs.eclipse.org/bugs/show_bug.cgi?id="

f = open('bug_shas.dat', 'r')
f1 = open('mldata_filtered', 'r')
f2 = open('final_out_bug_list.dat', 'w')

flist = []
for line in f1:
	flist.append(line.split(',')[0].strip('\s'))

bug_list = dict()
def get_message(r, sha):
	global url
	try:
		message = r.get_commit(sha).commit.message
		print message
		if re.search('Bug\s|bug\s|Fix\s|fix\s', message):
			reportdate = None
			m = re.search('Bug\s[0-9]*|bug\s[0-9]*|Fix\sfor\s[0-9]*|fix\sfor\s[0-9]*|Fixed\s[0-9]*|fixed\s[0-9]*', message)
			if m:
				bugid = m.group(0).split(' ').pop().strip()
				print "Bug #" + bugid
				urltemp = url + bugid
				data = []
				for line in urllib.urlopen(urltemp):
					data.append(line)
				parsing = False
				for line in data:
					if parsing == False:
						if re.search('<b>\s*Reported\s*</b>:', line):
							print "Reported matched"
							parsing = True
					elif parsing == True:
						m = re.search('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', line)
						if m:
							datestring = m.group(0)
							print datestring
							[y, m, d] = datestring.split('-')
							reportdate = date(int(y), int(m), int(d))
							break
			if reldate <= reportdate <= fdate:
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
