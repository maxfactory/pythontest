import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
	rw = RandomWalk(5000)
	rw.fill_walk()

	# 设置绘图窗口的大小
	plt.figure(dpi=128,figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
		# edgecolors='none', s=1)
	plt.plot(rw.x_values, rw.y_values, linewidth=2)
	# 突出起点和终点
	plt.scatter(0,0,c='blue', edgecolors='none',s=10)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none',s=100)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_runing = input("Make anthor walk?(y/n):")
	if keep_runing == 'n':
		break