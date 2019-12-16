# 1.获得用户输入的一个整数N，计算并输出N的32次方。
n = eval(input("请输入一个数："))
#(1)
# a = n ** 32
# print(a)
#(2)
i = 1
a = n
while i < 32:
	a *= n
	i += 1
print(a)