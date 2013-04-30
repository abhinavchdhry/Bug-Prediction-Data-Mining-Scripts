import os, sys, re
datafile = open('data_3_0_3_1_final.dat', 'r')
dump = open('data3_0_3_1.dat', 'w')

files = []
for f in os.listdir('.'):
	if f.endswith('.txt'):
		files.append(f)

clusters = []
for f in files:
	fh = open(f, 'r')
	temp = []
	for line in fh:
		if re.search('^FILENAME', line):
			fname = line.split(' ').pop().split('/').pop().strip(' \n')
			if fname.endswith('.java'):
				temp.append(fname)
	clusters.append(temp)

remove = []
for i in range(len(clusters)-1, -1, -1):
	if not clusters[i]:
		del(clusters[i])

currentfiles = []
array = []
for line in datafile:
	array.append(line.split(','))
	currentfiles.append(line.split(',')[0].strip(' \n'))

maxChangeSet = dict()
avgChangeSet = dict()

for f in currentfiles:
	count = 0
	total = 0
	for cluster in clusters:
		if f in cluster:
			total += len(cluster)
			count += 1
			if f in maxChangeSet:
				if len(maxChangeSet[f]) < len(cluster):
					maxChangeSet[f] = cluster
			else:
				maxChangeSet[f] = cluster
	avgChangeSet[f] = float(total)/float(count)

for x in maxChangeSet:
	maxChangeSet[x] = len(maxChangeSet[x])

for i in range(0,len(array)):
	out = array[i].pop().strip()
	array[i].append(str(maxChangeSet[array[i][0].strip()]))
	array[i].append(str(avgChangeSet[array[i][0].strip()]))
	array[i].append(out)
	dump.write(','.join(array[i]))
	dump.write('\n')
