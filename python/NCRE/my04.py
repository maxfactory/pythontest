import random
for i in range(10):
    a = random.choice(range(10))    #从0到9中随机挑选一个整数
    print(a)
print('*'*20)
for i in range(10):
    a = random.randrange(1,10)     #从指定范围内，按指定其数递增的集合中获取一个随机数
    print(a)
print('*'*20)
for i in range(10):
    a = random.random()             #随机生成下一个实数，在(0,1)范围内
    print(a)
print('*'*20)
for i in range(10):
    a = random.uniform(5,8)         # 在指定的范围内生成一个随机实数
    print(a)
print('*'*20)
li = list(range(10))
random.shuffle(li)                  # 将序列的所有元素随机排序
print(li)
print("*"*20)
num = list(range(10))
new = random.sample(num,5)          # 随机获取指定长度的片段
print(new)
print("*"*20)
for i in range(10):
    a = random.randint(6,60)        # 随机生成指定范围内的整数，参数为int型
    print(a)
