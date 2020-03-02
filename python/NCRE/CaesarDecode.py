etxt = input("请输入加密后文本：")
for p in etxt:
    if "a" <= p <= "z":
        print(chr(ord("a") + (ord(p) - ord("a") -6) %26),end='')
    elif "A" <= p <= "Z":
        print(chr(ord("A") + (ord(p) - ord("A") -6) %26),end='')
    else:
        print(p,end='')
