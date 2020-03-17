# for循环和if条件语句去对数据进行判断，判断是否为质数并打印出来

for x in range(10,15):		# 迭代10--15之间的数字
	for i in range(2,x):	# 根据因子迭代
		if x%i == 0:		# 确定第一个因子
			j=x/i 			# 计算第二个因子
			print('%d 等于 %d * %d' % (x,i,j))
			break			# 跳出当前循环
	else:
		print(x,'是一个质数')