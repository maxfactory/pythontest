import time
time1 =time.time()
a = ""
for i in range(100000000):
	a += 'six'
time2 = time.time()
print("运行时间：" + str(time2 - time1))

time3 = time.time()
li = []
for i in range(100000000):
	li.append('six')
a = ''.join(li)
time4 = time.time()
print("运行时间：" + str(time4 - time3))