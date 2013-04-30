import os, re, dateutil.parser
from datetime import date, timedelta
import math

f = open('final_data.dat', 'r')
filelist = []
filedates = dict()
date1 = date(2010, 6, 8)
date2 = date(2011, 6, 13)

for line in f:
	filelist.append(line.split(',').pop().strip(' \n'))

for content in os.listdir('.'):
	if content.endswith('.txt'):
		f = open(content, 'r')
		d = None
		for line in f:
			if re.search('^DATE', line):
	#			print line
				d = dateutil.parser.parse(line.split(' ').pop().strip(' \n')).date()
			if re.search('^FILENAME', line) and d != None:
				fname = line.split('/').pop().strip(' \n')
				if fname in filedates:
					filedates[fname].append(d)
				else:
					filedates[fname] = []
					filedates[fname].append(d)

#for f in filedates:
#	filedates[f].sort()
#	print f, filedates[f]
#	print '\n'

# Calculate max burst size, gap size = 30 days
# Definition: 	This feature is defined as ...
#		MaxBurstSize/AvgBurstGapOfMaxBurst

for f in filedates:
	datelist = filedates[f]
	datelist.sort()
	longest_span_starting_here = []
	for i in range(0,len(datelist)):
		count = 0
		end = datelist[i] + timedelta(days=30)
		for j in range(i+1, len(datelist)):
			if datelist[j] <= end:
				count += 1
		longest_span_starting_here.append(count)
	maxspansize = max(longest_span_starting_here)
	index = None
	for i in range(len(longest_span_starting_here)-1, -1, -1):
		if longest_span_starting_here[i] == maxspansize:
			index = i
			break
	gapSum = 0
	for i in range(index, index+maxspansize-1):
		gapSum += (datelist[i+1]-datelist[i]).days
#	if maxspansize >= 2:
#		AvgBurstGap = float(gapSum)/float(maxspansize-1)
#		if AvgBurstGap != 0:
#			avg = float(maxspansize)/float(AvgBurstGap)
#			print f, avg
#		else:
#			print f, str(0.0)
	print f, maxspansize
#	else:
#		print f, str(0.0)

def revisedLog(x, y):
	if x == 0:
		return 0
	else:
		return math.log(x, y)
	
# Calculate change entropy per file
period_len = (date2 - date1).days/12
#print 'Period: ' + str(period_len)

for f in filedates:
	end = date1
	periodic_changes = []
	for i in range(1,12):
		start = end
		end = start + timedelta(days=period_len)
		count = 0
#		print 'Start: ' + str(start) + ' End: ' + str(end)
		for dt in filedates[f]:
			if start < dt <= end:
				count += 1
		periodic_changes.append(count)
	start = end
	end = date2
	count = 0
#	print 'Start: ' + str(start) + ' End: ' + str(end)
	for dt in filedates[f]:
		if start < dt <= end:
			count += 1
	periodic_changes.append(count)
	
	total = sum(periodic_changes)
	if total == 0:
		print f, periodic_changes
	for i in range(0, len(periodic_changes)):
		periodic_changes[i] = float(periodic_changes[i])/float(total)
	entropy = 0.0
	expected_period = 0.0
	for x in range(1,13):
		expected_period += periodic_changes[x-1]*x

	for c in periodic_changes:
		entropy += c*revisedLog(c, 2)
	entropy *= (-1)
#	print f, entropy
#	print f, expected_period

#	print f,
#	for p in periodic_changes:
#		print p,
#	print '\n'

