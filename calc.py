import sys
f = open('accuracy','r')

sum = 0.0
count = 0
for line in f:
	val = float(line.split(' ')[1].strip(' \n'))
	sum += val
	count += 1

average = float(sum)/float(count)
print 'Average: ' + str(average)
