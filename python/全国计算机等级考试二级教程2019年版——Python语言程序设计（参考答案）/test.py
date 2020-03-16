l1 = []
l2 = []
for i in range(100):
    if i % 6 == 1:
       l1.append(i)
    elif i % 6 == 5:
        l2.append(i)

print("l1:{0}\nl2:{1}".format(l1,l2))
