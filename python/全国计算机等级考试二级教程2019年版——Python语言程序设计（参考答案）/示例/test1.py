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


"""def sum(n):
	if n==1:
		return 1
	else:
		return n+sum(n-1)
print(sum(2))"""

# def addOne(a):
# 	print(id(a),':',a)
# 	a+=1
# 	print(id(a),':',a)

# v=3
# print(id(v))
# addOne(v)
# print(id(v))

# try:
#    n = 0
#    n = input("请输入一个整数: ")
#    def pow10(n):
#       return n**10
# except:
#    print("程序执行错误")



# try:
# 	def pow10(n):
# 		return n*2
# except:
# 	print("程序执行错误")

# n = input("请输入一个整数: ")
# print(pow10(n))


# a = [[1,2,3], [4,5,6], [7,8,9]]
# s = 0 
# for c in a:
#    for j in range(3):
#       s += c[j]
# print(s)

# for x in range(1,10):
# 	for y in range(1,x+1):
# 		print("{0} * {1} = {2}".format(y,x,x*y),end='\t')
# 	print()
	# print(x)


# txt = open("C:\\Users\\Administrator\\Desktop\\test.txt", "r")
# print(txt)
# txt.close()


# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# num =eval(input("请输入一个整数："))
# print(fact(abs(int(num))))


import turtle as t
def DrawCctCircle(n):
	t.penup()
	t.goto(0,-n)
	t.pendown()
	t.circle(n)
for i in range(20,80,20):
	DrawCctCircle(i)
t.done()

