"""
摄氏温度：c = (F-32)/1.8
华氏温度：F = C*1.8 +32
"""

# str = input("请输入一个温度（如：32C）：")
# if str[-1] in ('C','c'):
#     F = float(str[0:-1]) * 1.8 + 32
#     print("摄氏度转换成华氏度为：",F)
# elif str[-1] in ('F','f'):
#     C = (float(str[0:-1]) - 32) / 1.8
#     print("华氏底转换成摄氏度为：",C)
# else:
#     print("请输入正确的值！")

val = input("请输入带有温度表示符号的温度值(例如：32C)：")
if val[-1] in ('C','c'):
	f = 1.8*float(val[0:-1]) + 32
	print("转换后的温度为:%.2fF"%f)
elif val[-1] in('F','f'):
	c = (float(val[0:-1])-32)/1.8
	print("转换后的温度为：%.2fC"%c)
else:
	print("输入错误，请输入正确的值")

#-*-coding:utf-8-*-