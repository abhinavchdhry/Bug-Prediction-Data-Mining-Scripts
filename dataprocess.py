import random
from sklearn import tree, svm
from sklearn.ensemble import RandomForestClassifier

fil = 'final_data.dat'

fhandle = open(fil, 'r')
final = []	# Final attr list
output = [] 	# Final output values corresponding to final data list

initData = []
for line in fhandle:
	initData.append(line)

UseSVM = False
# Randomly shuffle 10 times and train on the first 2/3 of the values and test on 1/3 of the values

if UseSVM == False:
	random.shuffle(initData)
	for line in initData:
		li = []
		for data in line.split(','):
			li.append(data.strip(' \n'))
		li.pop(0)
		out = li.pop()
		for j in range(0,len(li)):
			li[j] = int(li[j])
		final.append(li)
		output.append(out)

	for i in range(0,len(output)):
		if output[i] == 'YES':
			output[i] = 1
		else:
			output[i] = 0

	trainData = []
	trainOutput = []
	testData = []
	testOutput = []

#	clf = tree.DecisionTreeClassifier()
	clf = RandomForestClassifier(n_estimators=10)

	for i in range(0,int(len(output)*2/3)):
		trainData.append(final[i])
		trainOutput.append(output[i])
	
	for j in range(int(len(output)*2/3), len(output)):
		testData.append(final[j])
		testOutput.append(output[j])

	print 'Training...'
	clf = clf.fit(trainData, trainOutput)
	print '...Done'

	total = len(testOutput)
	correct = 0
	testResult = clf.predict(testData)

	if len(testResult) == len(testOutput):
		for i in range(0,len(testResult)):
			if testResult[i] == testOutput[i]:
				correct += 1

	print 'Accuracy: ' + str(float(correct)/float(total))

elif UseSVM == True:
	random.shuffle(initData)
	for line in initData:
		li = []
		for data in line.split(','):
			li.append(data.strip(' \n'))
		li.pop(0)
		out = li.pop()
		for j in range(0,len(li)):
			li[j] = int(li[j])
		final.append(li)
		output.append(out)

	for i in range(0,len(output)):
		if output[i] == 'YES':
			output[i] = 1
		else:
			output[i] = 0

	trainData = []
	trainOutput = []
	testData = []
	testOutput = []

	clf = svm.SVC()
	
	for i in range(0,int(len(output)*2/3)):
		trainData.append(final[i])
		trainOutput.append(output[i])
	
	for j in range(int(len(output)*2/3), len(output)):
		testData.append(final[j])
		testOutput.append(output[j])

	print 'Training...'
	clf.fit(trainData, trainOutput)
	print '...Done'

	total = len(testOutput)
	correct = 0
	testResult = clf.predict(testData)

	if len(testResult) == len(testOutput):
		for i in range(0,len(testResult)):
			if testResult[i] == testOutput[i]:
				correct += 1

	print 'Accuracy: ' + str(float(correct)/float(total))
