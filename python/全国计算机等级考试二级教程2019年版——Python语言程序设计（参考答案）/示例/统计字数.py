filename = r'C:\Users\max\Desktop\my.txt'
li = []
# bd = ['，','。','“','”','、','……','！','‘','’','《','》','？','（','）']
bd = []
with open(filename) as f_obj:
	lines = f_obj.readlines()
	strings = ''
	for line in lines:
		strings += line.strip()
	for i in strings:
		if i in bd:
			continue
		else:
			li.append(i)
	num_word = len(li)
	print(num_word)
	print(strings)
	print(li)