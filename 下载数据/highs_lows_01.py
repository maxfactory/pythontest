import csv
#
filename = "PTA060211DX.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highs = []
	for row in reader:
		highs.append(row[1])

	print(highs)