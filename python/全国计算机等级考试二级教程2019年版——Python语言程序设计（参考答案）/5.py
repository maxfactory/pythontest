# 5.获得用户输入的一个整数N，计算并输出1到N相加的和。
n = eval(input("请输入n："))
sum = 0
for i in range(n+1):
	sum += i
print(sum)