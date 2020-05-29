# 编写代码，模拟决赛现场最终成绩的计算过程

while True:
    try:
        n = int(input('请输入评委人数：'))
        if n <= 2:
            print('评委人数太少，必须多于两个人。')
        else:
            break
    except:
        pass
scores = []
"""print('第一种写法：')"""
for i in range(n):
    # 这个while循环用来保证用户必须输入0-100之间的数字
    while True:
        try:
            score = input('请输入第{0}个评委的分数：'.format(i + 1))
            # 把字符串转换为实数
            score = float(score)
            assert 0 <= score <= 100
            scores.append(score)
            # 如果数据合法，跳出while循环，继续输入下一个评委的分数
            break
        except:
            print('分数错误！')

"""print('第二种写法，这种写法必须要加上try...except，否则最到空值时会报错：')"""
# for i in range(n):
# 	while True:
# 		score = input('请输入第{0}个评委的分数：'.format(i+1))
# 		score = float(score)
# 		if 0<=score<=100:
# 			scores.append(score)
# 		else:
# 			print('分数错误！')
# 			continue
# 		break

"""没有try....except，直接这样写是错的。"""
# for i in range(n):
# 	# 这个while循环用来保证用户必须输入0-100之间的数字
# 	while True:
# 		score = input('请输入第{0}个评委的分数：'.format(i+1))
# 		# 把字符串转换为实数
# 		score = float(score)
# 		assert 0<=score<=100
# 		scores.append(score)
# 		# 如果数据合法，跳出while循环，继续输入下一个评委的分数
# 		break

# 计算并删除最高分与最低分
highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)
finalscore = round(sum(scores) / len(scores), 2)

formatter = "去掉一个最高分{0}\n去掉一个最低分{1}\n最后得分{2}"
print(formatter.format(highest, lowest, finalscore))