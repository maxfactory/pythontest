filename = r"C:\Users\Administrator\Desktop\test.txt"
li = []
with open(filename) as t_obj:
    contents = t_obj.readline()
    for i in contents:
        li.append(i)
    word = len(li)
    print(li)
    print(word)
