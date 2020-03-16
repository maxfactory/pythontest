#编写代码，输出由星号*组成的菱形图案，并且可以灵活控制图案的大小
def main(n):
	for i in range(n):
		print((" * " * i).center(n*3))
	for i in range(n,0,-1):
		print((" * " * i).center(n*3))
main(0)