x = input("input two number:")
a,b = map(int, x.split())
if a > b:
    a, b = b, a
print(a, b)
