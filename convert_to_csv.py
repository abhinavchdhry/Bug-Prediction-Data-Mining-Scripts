name = 'data3_0_3_1.dat'
f = open(name, 'r')
out = open(name.split('.')[0]+'.csv', 'w')

header = ['commits','adds','dels','authors','commits60','lastcommit','indevbugs','entropy','MPC','maxburst','maxchangeset','avgchangeset','output']
data = []
for line in f:
	temp = line.split(',')
	del(temp[0])
	for i in range(0,len(temp)):
		temp[i] = temp[i].strip(' \n')
	data.append(temp)

out.write(','.join(header))
out.write('\n')

for line in data:
	out.write(','.join(line))
	out.write('\n')
