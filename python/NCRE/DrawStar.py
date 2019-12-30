"""绘制五角红星
用Python程序绘制一个五角红星图形。"""
from turtle import *
# color('red','red')
# hideturtle()		# 隐藏画笔
# begin_fill()
# for i in range(5):
# 	fd(200)
# 	rt(144)
# end_fill()
# done()

i = 5
color('red','red')
hideturtle()
begin_fill()
# end_fill()
while i > 0:
	fd(200)
	rt(144)
	i -= 1
end_fill()
done()


# from turtle import *
# color('red','red')
# # fillcolor('red')  # 设置填充颜色为红色
# hideturtle()  # 隐藏箭头显示
# begin_fill()  # 开始填充
# while True:
#     forward(200)  
#     right(144)
#     if abs(pos())<1:
#         break
# end_fill()  # 结束填充
# penup()  # 笔尖朝上（无痕）
# fd(-100)  # 后退100像素
# pendown()  # 笔尖朝下（有痕）
# write('Five-points Star',font=('Times New Roman','15','bold'))
# done()