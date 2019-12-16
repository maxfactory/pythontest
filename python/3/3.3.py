cars = ['bmw','audi','toyota','subaru']
# 使用方法sort()对列表进行永久性排序
cars.sort()
print(cars)
# 按字母顺序相反的方向排序
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
# 使用函数sorted()对列表进行临时排序
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars,reverse=True))
print(cars)

cars = ['bmw','audi','toyota','subaru']
# 倒着打印列表
cars.reverse()
print(cars)