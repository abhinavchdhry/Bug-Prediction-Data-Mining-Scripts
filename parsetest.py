import re, urllib

sample = "HEAD- Fixed bug 353085: [1.7] Cannot cast from Object to boolean"
url = "https://bugs.eclipse.org/bugs/show_bug.cgi?id="

m = re.search('bug\s[0-9]*|Bug\s[0-9]*', sample)
id = None
if m:
	id = m.group(0).split(' ').pop().strip()
	
url += id

page = []
for line in urllib.urlopen(url):
	page.append(line)
	
parsing = False
for line in page:
	if parsing == False:
		m = re.search('<b>Reported</b>:', line)
		if m:
			parsing = True
	elif parsing == True:
		m = re.search('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', line)
		if m:
			parsing = False
			print m.group(0)
			break
