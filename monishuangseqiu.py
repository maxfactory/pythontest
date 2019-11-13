import random
red_nums = set()
while True:
	red_num = int(random.random() * 34)
	if red_num == 0:
		continue
	else:
		red_nums.add(red_num)
	if len(red_nums) == 6:
		break

rn = sorted(red_nums)
double_ball = list(rn)

while True:
	blue_num = int(random.random() * 17)
	if blue_num != 0:
		break

double_ball.append(blue_num)
print(double_ball)