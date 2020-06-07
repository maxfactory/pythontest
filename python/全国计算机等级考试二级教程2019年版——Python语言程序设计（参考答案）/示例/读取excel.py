import pandas as pd
file = r'C:\Users\Administrator\Desktop\test.xlsx'
data = pd.read_excel(file)
data.head()

print(data)