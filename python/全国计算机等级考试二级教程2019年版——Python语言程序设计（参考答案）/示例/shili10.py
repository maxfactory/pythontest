#Python允许函数的嵌套定义，在函数内部可以再定义另外一个函数
def myMap(interable,op,value):   #自定义函数
	if op not in '+-*/':
		return 'Error operation'
	def nested(item):			#嵌套定义函数
		# return eval(repr(item)+op+repr(value))
		return eval(repr(item)+op+repr(value))

	return map(nested,interable)		#使用在函数内部定义的函数

# a = list(myMap(1,'+',5))
a = myMap(range(5),'+',5)

print(a)