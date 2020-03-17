# 利用嵌套循环对数组num里面的值进行修改，重新赋值为i*j

import numpy
num = numpy.zeros(shape=(3,3))
for i in range(0,3):
	for j in range(0,3):
		num[i,j] = i*j

print(num)