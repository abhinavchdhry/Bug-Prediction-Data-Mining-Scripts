bugfile1 = open('final_indev_bug_list.dat', 'r')
bugfile2 = open('final_bug_list.dat', 'r')
datafile = open('mldata_filtered', 'r')
#finalout = open('final_data.out', 'w')

bugdict1 = dict()
bugdict2 = dict()

# LOW :: 0-4 bugs
# MED :: 5-9 bugs
# HIGH :: 10+ bugs

for line in bugfile1:
	fname = line.split(',')[0].strip(' \n')
	bugs = line.split(',')[1].strip(' \n')
	if fname not in bugdict1:
		bugdict1[fname] = int(bugs)

for line in bugfile2:
	fname = line.split(',')[0].strip(' \n')
	bugs = line.split(',')[1].strip(' \n')
	if fname not in bugdict2:
		bugdict2[fname] = int(bugs)

l = []
for x in bugdict2:
	l.append(int(bugdict2[x]))
l.sort()

#for x in bugdict2:
#	if 0<= int(bugdict2[x]) <= 4:
#		bugdict2[x] = 'LOW'
#	elif 5 <= int(bugdict2[x]) <= 9:
#		bugdict2[x] = 'MED'
#	elif int(bugdict2[x]) >= 10:
#		bugdict2[x] = 'HIGH'

#print 'lowest = ' + str(l[0]) + 'highest = ' + str(l.pop())

data = []
for line in datafile:
	li = []
	for e in line.split(','):
		li.append(e.strip(' \n'))
	data.append(li)

semifinal = []
for l in data:
	if l[0] in bugdict1:
		l.append(str(bugdict1[l[0]]))
	else:
		l.append('0')
	semifinal.append(l)

final = []
for l in semifinal:
	if l[0] in bugdict2 and int(bugdict2[l[0]]) != 0:
		l.append('YES')
	else:
		l.append('NO')
	final.append(l)

for x in final:
	print ','.join(x)
