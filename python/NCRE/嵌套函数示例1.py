def myMap(interable,op,value):
    if op not in '+-*/':
        print("Error oprater!")
    def netse(item):
        return eval(repr(item)+op+repr(value))
    return map(netse,interable)
a = list(myMap(range(5),'+',5))
print(a)
