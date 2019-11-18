import csv
import matplotlib.pyplot as plt

filename = 'PTA060211DX.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highs = []
	for row in reader:
		high = float(row[1])
		highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')

# 设置图形的格式
plt.title("Daily high temperatures,July 2014", fontsize=24)
# plt.title("天气情况",fontsize=24, fontproperties='SimSun')
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()