# a, b = 0, 1
a = 0
b = 1
while a < 1000:
	print(a, end=',')    # a = 0
	a, b = b, a + b
	# a = b		# a = 1
	# b = a+b		# b = 1



	# temp = b
	# b = a+b
	# a = temp
	0,1
	1,1
	1,2
	2,3
	3,5
	5,8
	8,13
	13,21