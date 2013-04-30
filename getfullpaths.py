import os, re

f = open('final_data.dat','r')
searchpath = '/home/abhinav/Downloads/3.1/'
origpath = os.path.abspath('.')
final = open('fullpaths', 'w')

for line in f:
	fname = line.split(',')[0].strip(' \n')
	os.chdir(searchpath)
	os.system('find -L ' + fname + ' . > out.txt')
	tempf = open('out.txt', 'r')
	for l in tempf:
		if re.search('/'+fname,l):
			final.write(l)
os.chdir(origpath)
