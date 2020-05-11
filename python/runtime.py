import time
time1 =time.time()
a = ""
for i in range(1000000):
	a += 'cat'
# print(a)
time2 = time.time()
print("运行时间：" + str(time2 - time1))

time3 = time.time()
b = ''
li = []
for i in range(1000000):
	li.append('cat')
b = ''.join(li)
# print(b)
time4 = time.time()
print("运行时间：" + str(time4 - time3))