import os, re,sys

JCSC_BIN = '/home/abhinav/Downloads/jcsc/bin/'
CURPATH = os.path.abspath('.')

f = open('fullpaths.dat', 'r')
os.chdir(JCSC_BIN)
dataout = open('staticdata.dat', 'w')

for fname in f:
	print fname
	out = os.popen('./jcsc.sh '+fname).readlines()

	startparsing = False
	ccn = []
	NCSS = None
	LC = None
	MC = None
	for line in out:
		if re.search('Metrics:', line):
			startparsing = True
		elif startparsing==True:
			if re.search('CCN-', line):
				cn = int(line.split('-').pop().strip())
				print 'CN is '+ str(cn)
				ccn.append(cn)
			elif re.search('NCSS count', line):
				NCSS = int(line.split(':').pop().strip())
			elif re.search('Lines count', line):
				LC = int(line.split(':').pop().strip())
				print LC
			elif re.search('Methods count', line):
				MC = int(line.split(':').pop().strip())
				print MC
	if MC != 0:
		avgCCN = float(sum(ccn))/float(MC)
	else:
		avgCCN = 0
	fnamestripd = fname.split('/').pop().strip()
	dataout.write(fnamestripd+', '+str(NCSS)+', '+str(LC)+', '+str(MC)+', '+str(avgCCN)+'\n')
dataout.close()
