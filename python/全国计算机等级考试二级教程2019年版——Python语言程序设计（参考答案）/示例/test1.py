"""#循环语句完成：
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



def recursion(n):
    v = n//2 # 地板除，保留整数
    print(v) # 每次求商，输出商的值
    if v==0:
        ''' 当商为0时，停止，返回Done'''
        return 'over'
    recursion(v) # 递归调用，函数内自己调用自己
recursion(10) # 函数调用


def ss(n):
	if n == 1:
		return 1
	else:
		return n+ss(n-1)

print(ss(2))



"""


def sum(n):
	if n==1:
		return 1
	else:
		return n+sum(n-1)
print(sum(2))