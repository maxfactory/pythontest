# 编写程序，计算组合数C(n,i)，即从n个元素中任选i个，有多少种选法
def Cni(n,i):
	if not (isinstance(n,int) and isinstance(i,int) and n>=i):
		print('n and i must be integers and n must be larger than or equal to i.')
		return
	result = 1
	Min, Max = sorted((i,n-i))
	print("Min=",Min,"Max=",Max)
	for i in range(n,0,-1):		# 8 7 6 5 4 3 2 1
		if i > Max:				# 8 7
			result *= i
		elif i <= Min:			# 2 1 
			result /= i
	return result

print(int(Cni(8,3)))

# print("**"*20)

# def Cni(n,i):
# 	if not (isinstance(n,int) and isinstance(i,int) and n>=i):
# 		print('n and i must be integers and n must be larger than or equal to i.')
# 		return
# 	else:
# 		result = 1
# 		re = 1
# 		for x in range(n):
# 			result *= x
# 		