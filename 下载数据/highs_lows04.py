import csv
import matplotlib.pyplot as plt
from datetime import datetime
# 从文件中攻取日期、最高气温和最低气温
filename = 'PTA060211DX.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs,lows = [],[],[]
	# dates,highs,lows,others,aa,bb = [],[],[],[],[],[]
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y/%m/%d")
		dates.append(current_date)

		high = float(row[1])
		highs.append(high)

		low = float(row[3])
		lows.append(low)

		# other = float(row[5])
		# others.append(other)

		# a = float(row[7])
		# aa.append(a)

		# b = float(row[9])
		# bb.append(b)

#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.plot(dates, others, c='brown')
# plt.plot(dates, aa, c='green')
# plt.plot(dates, bb, c='pink')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# plt.fill_between(dates,aa,bb,facecolor='red',alpha=0.1)

# 设置图形格式
plt.title("Daily htgh and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()