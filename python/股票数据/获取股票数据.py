import tushare as ts
import pandas as pd
import time
import os.path

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))

file = 'D:\\stock\\stock_data'+year+'_'+month+'_'+day+'.csv'
stock_data = ts.get_today_all()
stock_data.to_csv(file)
# localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print('localtime='+localtime)

# year = time.strftime('%Y',time.localtime(time.time()))
# month = time.strftime('%m',time.localtime(time.time()))
# day = time.strftime('%d',time.localtime(time.time()))
# print(year,month,day)