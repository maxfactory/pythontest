#Python允许函数的嵌套定义，在函数内部可以再定义另外一个函数
def myMap(inter,op,value):   #自定义函数
	if op not in '+-*/':
		return 'Error operation'
	def nested(item):			#嵌套定义函数
		# repr() 函数将对象转化为供解释器读取的形式
		return eval(repr(item)+op+repr(value))
		# return eval(item + op + value)
	"""
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，
返回包含每次 function 函数返回值的新列表。
语法：map(function, iterable, ...)
	"""
	return map(nested,inter)		#使用在函数内部定义的函数

a = list(myMap(range(5),'+',5))
# a = myMap(range(5),'+',5)

print(a)