import os, re
from datetime import date, timedelta
import dateutil.parser

set1 = set(line.strip() for line in open('list3_6.dat', 'r'))
set2 = set(line.strip() for line in open('list3_7.dat', 'r'))

enddate = date(2011, 6, 13)
start = date(2010, 6, 8)

out = open('mldata', 'w')
common = []
for f in set1 and set2:
	common.append(f)

commitlist = []
for x in os.listdir('.'):
	if x.endswith('.txt'):
		commitlist.append(x)

def get_commit_freq_and_additions(f, commitlist):
	count = 0
	additions = 0
	deletions = 0
	authorlist = []
	for c in commitlist:
		parsing = False
		for line in open(c, 'r'):
			if re.search('AUTHOR', line):
				author = line.split(' ').pop()
			if re.search('FILENAME', line):
				fullpath = line.strip('\n').split(' ')[1]
				name = fullpath.split('/').pop()
				if name == f:
					count += 1
					parsing = True
					if author not in authorlist:
						authorlist.append(author)
			if parsing == True and re.search('ADD', line):
				additions += int(line.split(' ').pop())
			if parsing == True and re.search('DEL', line):
				deletions += int(line.split(' ').pop())
				break
	return [count, additions, deletions, len(authorlist)]

def get_CF_last_60_days(f, commitlist):
	count = 0
	startdate = enddate - timedelta(days=200)
	most_recent = start
	for c in commitlist:
		parsing = False
		for line in open(c, 'r'):
			if re.search('DATE', line):
				d = dateutil.parser.parse(line.split(' ').pop()).date()
				if d>=startdate and d<=enddate:
					parsing = True
				else:
					break
			if parsing==True and re.search('FILENAME', line):
				if f==line.split(' ').pop().strip('\n').split('/').pop():
					count += 1
					if d > most_recent and d <= enddate:
						most_recent = d
					break
	diff = (enddate-most_recent).days
	return [count, diff]
	
for f in common:
	print f, get_commit_freq_and_additions(f, commitlist), get_CF_last_60_days(f, commitlist)
