squares = []
for value in range(1,11):
	# square = value ** 2
	# squares.append(square)
	squares.append(value ** 2)
print(squares)

# 4.3.4 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
