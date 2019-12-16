#1.输入一个年份，输出是否是闰年。#闰年条件：能被4整除但不能被100整除，或者能被400整除的年份，
# 都是闰年。
# year = eval(input("请输入一个年份:"))
# if year % 4 == 0 and year % 100 != 0:
# 	print("闰年")
# elif year % 400 == 0:
# 	print("闰年")
# else:
# 	print("不是闰年")


year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))