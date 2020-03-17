##a=6
##li = []
##assert a>5
##li.append(a)
##print(li)


a = input('请输入一个浮点数：')
i = 0
while i < len(a):
    if a[i] == '.':
        print(a[0:i])
        break
    i += 1
if i == len(a):
    print(a)
