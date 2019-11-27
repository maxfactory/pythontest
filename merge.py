# Python使用9行代码批量合并Excel文件
import os
import pandas as pd
excels = [
	pd.read_excel(fname)
	for fname in os.listdir("./")
	if ".xlsx" in fname
]
df = pd.concat(excels)
df.to_excel("3.xlsx", index=False)