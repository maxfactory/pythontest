
def count_words(filename):
	try:
		with open(filename,encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		with open(filename,'w',encoding='utf-8') as f_obj:
			f_obj.write('This file is new.')
			print("Create a new file:" + filename + "." )
	else:
		if contents == 'This file is new.':
			print("The new file isn't need counting.")
		else:
			words = contents.split()
			num_words = len(words)
			print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice1.txt'
count_words(filename)