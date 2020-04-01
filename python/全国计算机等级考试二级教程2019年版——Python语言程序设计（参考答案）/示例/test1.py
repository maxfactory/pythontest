#循环语句完成：
def sum1(num):
	sum2=0
	for i in range(1,num+1):
		sum2+=i
	return sum2
 
print(sum1(100))
 
#递归完成
def sum_a(num1):
 
	if num1==1:
		return 1
	else:
		return num1+sum_a(num1-1)
 
print(sum_a(100))
