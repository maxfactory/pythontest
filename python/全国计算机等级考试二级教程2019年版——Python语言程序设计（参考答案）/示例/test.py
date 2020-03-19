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

a = 3
b = 5
try:
	assert a == b,'a must be equal to b'
except AssertionError as reason:
	print('%s:%s'%(reason.__class__.__name__,reason))