import os, re, sys
from datetime import date, timedelta
import dateutil.parser

release_date = date(2005, 6, 27)
date_60days_before = release_date - timedelta(days=60)
start_date = date(2004, 6, 25)

common = []
set1 = set(line.strip('\n') for line in open('list3_0.dat', 'r'))
set2 = set(line.strip('\n') for line in open('list3_1.dat', 'r'))
#for line in set1 and set2:
#	common.append(line)

common = list(set1 & set2)

files = []
for f in os.listdir('.'):
	if f.endswith('.txt'):
		files.append(f)

out = open('mldata', 'w')

files_affected = dict()	# Keeps a dict of filenames and no. of commits affecting the file
file_additions = dict()	# Keeps a dict of filenames and no. of lines added within timeline
file_deletions = dict()	# Keeps a dict of filenames and no. of lines added within timeline
file_authors = dict()	# Keeps a dict of filenames and the list of authors involved in commits to the file
file_changes_last60days = dict() # Keeps a dict of filenames and the no. of commits in the last 60 days
last_file_change = dict() # Keeps a dict of filenames and no. of days before release when the last change was made

for f in files:
	fh = open(f, 'r')
	print f
	parsing = False
	for line in fh:
		if re.search('AUTHOR', line):
			author = line.split(' ').pop().strip('\n')
			continue
		if re.search('^DATE\s', line):
			d = line.split(' ').pop().strip('\n')
			print 'date:' + d
			date = dateutil.parser.parse(line.split(' ').pop().strip('\n')).date()
			continue
		if re.search('FILENAME', line):
			parsing = True
			filename = line.split(' ').pop().strip('\n').split('/').pop()
			if filename in files_affected:
				files_affected[filename] += 1
			else:
				files_affected[filename] = 1

			if filename in file_authors:
				if author not in file_authors[filename]:
					file_authors[filename].append(author)
			else:
				file_authors[filename] = list()
				file_authors[filename].append(author)

			if filename not in last_file_change:
				last_file_change[filename] = date
			elif date > last_file_change[filename] and date <= release_date:
				last_file_change[filename] = date

			if date > date_60days_before and date <= release_date:
				if filename in file_changes_last60days:
					file_changes_last60days[filename] += 1
				else:
					file_changes_last60days[filename] = 1
			continue
		if parsing==True and re.search('ADD', line):
			additions = int(line.split(' ').pop().strip('\n'))
			if filename in file_additions:
				file_additions[filename] += additions
			else:
				file_additions[filename] = additions
			continue
		if parsing == True and re.search('DEL', line):
			deletions = int(line.split(' ').pop().strip('\n'))
			if filename in file_deletions:
				file_deletions[filename] += deletions
			else:
				file_deletions[filename] = deletions
			continue
		if parsing==True and re.search('PATCH', line):
			parsing = False
			continue

def debug_print():
	for key in files_affected:
		print key, files_affected[key]

for f in common:
	data = []
	data.append(f)
	if f in files_affected:
		data.append(str(files_affected[f]))
	else:
		data.append('0')
	if f in file_additions:
		data.append(str(file_additions[f]))
	else:
		data.append('0')
	if f in file_deletions:
		data.append(str(file_deletions[f]))
	else:
		data.append('0')
	if f in file_authors:
		data.append(str(len(file_authors[f])))
	else:
		data.append('0')
	if f in file_changes_last60days:
		data.append(str(file_changes_last60days[f]))
	else:
		data.append('0')
	if f in last_file_change:
		data.append(str((release_date - last_file_change[f]).days))
	else:
		data.append('0')
	out.write(','.join(data))
	out.write('\n')
	print f + '...written to file.'
out.close()
