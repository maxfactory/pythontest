# li = [10,20,30,40,23,2000,1000]
li = []

while True:
	sz = input("请输入数字：")
	if sz == 'q' or sz == 'Q' or sz == '':
		break
	else:
		li.append(sz)
max = li[0]
min = li[0]
for i in range(len(li)):
	if int(li[i]) > int(max):
		max = li[i]
	if int(li[i]) < int(min):
		min = li[i]
print('最大值是：'+max + "\n"+"最小值是："+min)