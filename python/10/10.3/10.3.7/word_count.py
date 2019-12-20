# 使用多个文件
def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename,encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		# print("Sorry,the file " + filename + " does not exist.")
		# 如果想在此时什么也不做
		pass
	else:
		# 计算文件大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)
filenames = ['alice.txt','gtzylcd.txt','sj.txt']
for filename in filenames:
	count_words(filename)