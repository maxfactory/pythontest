##a=6
##li = []
##assert a>5
##li.append(a)
##print(li)


##a = input('请输入一个浮点数：')
##i = 0
##while i < len(a):
##    if a[i] == '.':
##        print(a[0:i])
##        break
##    i += 1
##if i == len(a):
##    print(a)
import time
time1 = time.time()

n = 2
a = n
i = 1
while i<1000:
    a *= n
    i += 1
print(a)
time2 = time.time()
print(time2-time1)

time3 = time.time()
a = 2
i = a**1000
print(i)
time4 = time.time()
print(time4-time3)
