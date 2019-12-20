filename = 'alice.txt'
try:
	"""
	在处理有中文字符的文档时报：
	UnicodeDecodeError: 'gbk' codec can't decode byte 0x83 in position 20: illegal multibyte sequence
	是当内部编码转化成 gbk编码（默认）时出错，我也不知道为啥，改为utf-8就好了
	只要在对文件进行操作时，加上 encoding='utf-8' 即可
	"""
	with open(filename, encoding='utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry,the file " + filename + " does not exist."
	print(msg)
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	# num_words = len(contents)
	print("The file " + filename + " bas about " + str(num_words) + " words.")