# # 找出1--100之间的所有质数
# flag=0
# for x in range(1,101):
# 	for y in range(2,x):
# 		if x%y==0:
# 			flag=1
# 			break
# 		else:
# 			flag=0
# 	if flag==0 and x!=1:
# 		print(x)

# for i in range(1,11):
# 	print(i)
# print(i)

# i=1
# while i<10:
# 	print(i)
# 	i += 1
# 	# if i >10:
# 	# 	break
# print(i)

# year = 1997
# for i in range(100):
# 	year += 3
# 	print(year,end=' ')


# year = 1997
# xx = input('是否继续： ')
# while xx == 'g':
# 	year += 3
# 	print(year)
# 	xx = input('是否继续： ')
# 	if xx != 'g':
# 		break

a = 0
b = 1
for i in range(12):
	a,b = a+b,a
	print(a, end=' ')