file1 = open('final_data.dat', 'r')
file2 = open('entropy.list', 'r')
outfile = open('data_with_entropy.dat', 'w')

data = []
entropy = []

for line in file1:
	l = line.split(',')
	for i in range(0,len(l)):
		l[i] = l[i].strip(' \n')
	data.append(l)

for line in file2:
	l = line.split(' ')
	for i in range(0,len(l)):
		l[i] = l[i].strip(' \n')
	entropy.append(l)

for l in data:
	fname = l[0]
	for e in entropy:
		if e[0] == fname:
			out = l.pop()
			l.append(e[1])
			l.append(out)
			break

for l in data:
	outfile.write(','.join(l))
	outfile.write('\n')
