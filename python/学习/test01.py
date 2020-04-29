# a = []
# for x in range(100):
# 	if x%9==0:
# 		a.append(x*2)
# print(a)



# a = [
# 	['高小一',18,30000,'北京'],
# 	['高小二',19,20000,'上海'],
# 	['高小三',20,10000,'深圳'],
# ]

# for m in range(3):
# 	for n in range(4):
# 		print(a[m][n],end='\t')
# 	print()

# r1 = {'name':'高小一','age':18,'salary':30000,'city':'北京'}
# r2 = {'name':'高小二','age':19,'salary':20000,'city':'上海'}
# r3 = {'name':'高小三','age':20,'salary':10000,'city':'深圳'}

# tb = [r1,r2,r3]

# # 获取第二行的人的薪资
# print(tb[1].get('salary'))

# # 打印表中所有的薪资
# for i in range(len(tb)):
# 	print(tb[i].get('salary'))

# # 打印表中的所有数据
# for i in range(len(tb)):
# 	print(tb[i].get('name'),tb[i].get('age'),tb[i].get('salary'),tb[i].get('city'))

a = pow(1500,1/3)
b = a **2
print(b)

c = 64.0**(1.0/3.0)
c=round(c)
# c=4**3
print(c)