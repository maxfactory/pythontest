# d = {'a':1,'b':2,'c':3}
# for x,y in d.items():
# 	print(x,y)
# for i in d:
# 	print(i)
# 	print(d[i])


"""for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)"""

"""列表解析"""
# val = map(lambda x:x*3,range(6))
# print(list(val))

# val1 = [x*3 for x in range(6)]
# print(val1)

# seq = [1,2,3,4,5,6,7,8]
# val3 = filter(lambda x:x%2,seq)
# print(list(val3))

# seq = [1,2,3,4,5,6,7,8]
# val4 = [x for x in seq if x%2]
# print(val4)

# t1 = [(i,j) for i in (0,3) for j in (0,3)]
# t2 = [{i,j} for i in (0,3) for j in (0,3)]
# t3 = [{i:j} for i in (0,3) for j in (0,3)]
# t4 = [[i,j] for i in (0,3) for j in (0,3)]

# print("元组：{0}\n集合：{1}\n字典：{2}\n列表：{3}".format(t1,t2,t3,t4))

# t = [(i,j) for i in (0,3) if i>2 for j in (0,3) if j<1]
# print(t)

# while True:
# 	try:
# 		a = input("请输入一个数：")
# 		if a.lower() == 'q':
# 			break
# 		assert int(a) > 50,'输入的数太小，请重输'
# 		print(a)
# 	except:
# 		# print("输入的数太小，请重输")
# 		continue

# a = 9
# assert a>10,'值太小！'
# print(a)

# a = 3
# b = 5
# try:
# 	assert a == b,'a must be equal to b'
# except AssertionError as reason:
# 	print('%s:%s'%(reason.__class__.__name__,reason))

# from random import randint
# def aaa(nu,li=[]):
# 	for i in range(2,int(nu**0.5)+1):
# 		if nu %i == 0:
# 			li.append(i)
# 			aaa(nu//i,li)
# 			break
# 	else:
# 		li.append(nu)

# lis = []
# n = randint(2,50)
# aaa(n,lis)
# result = '*'.join(map(str,lis))
# if n == eval(result):
# 	print(n,'=',result)
# print(n,'=',result)
# def maxmin(a,b):
# 	if a>b:
# 		return a,b
# 	else:
# 		return b,a
# big,small = maxmin(20,40)
# print(big,small)

#菲波那契数列
# def fib(n):
# 	a,b = 0,1
# 	while a<n:
# 		# print(a,end=' ')   #1
# 		a,b=b,a+b      #1 
# 		print(a,end=' ') 
# fib(1000)


# def fib(n):
# 	a,b = 1,1
# 	while a<n:
# 		print(a,end=' ')   #1
# 		a,b=b,a+b      #1 
# 		# print(a,end=' ') 
# fib(1000)


#Python允许函数的嵌套定义，在函数内部可以再定义另外一个函数
# def myMap(interable,op,value):   #自定义函数
# 	if op not in '+-*/':
# 		return 'Error operation'
# 	def nested(item):			#嵌套定义函数
# 		return eval(repr(item)+op+repr(value))
# 	return map(nested,interable)		#使用在函数内部定义的函数

# a = list(myMap(range(2),'+',5))
# print(a)


# for i in range(2):
# 	print(type(i))
# a = 8
# print(type(a))
# a = map(str,range(2))
# print(type(a))


# def myMap(inter,op,value):
# 	def nested(item):
# 		return eval(repr(item)+op+repr(value))
# 	return map(nested,inter)

# a = list(myMap(range(5),'+',5))
# print(a)

# # def myMap(inter,op,value):
# # 	return eval(repr(inter)+op+repr(value))
# # a = list(myMap(range(5),'+',5))
# # print(a)

# def nested(item):
# 		return eval(repr(item)+'+'+repr(5))
# a = list(map(nested,range(5)))
# print(a)

# def myMap(a,b,c):
# 	if b not in '+-*/':
# 		print("Error")
# 	def nested(d):
# 		return eval(str(d)+b+str(c))
# 	return map(nested,a)

# a = list(myMap(range(5),'*',5))
# print(a)


print("*"*20)
# def test(n):
# 	li = []
# 	for i in range(n):
# 		a = i *5
# 		li.append(a)
# 	else:
# 		print(li)	

# # print(li)
# test(5)

print("*"*20)

def atest(n):
	return n*3
a = list(map(atest,range(5)))
b = atest(5)
# a=atest(range(5))
print(a)
print(b)

