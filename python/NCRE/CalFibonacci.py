"""斐波那契数列的计算
F(0)=0， F(1)=1，
F(n)=F(n-2)+F(n-1)，其中n>=2"""
a, b = 0, 1
while a < 1000:
	print(a, end=',')
	a, b = b, a+b