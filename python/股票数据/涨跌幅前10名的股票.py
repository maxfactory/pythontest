import pandas as pd
import time
import os.path

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))

file = 'D:\\stock\\stock_data'+year+'_'+month+'_'+day+'.csv'
stock_data = pd.read_csv(file)

def get_top_10_perfomers():
    top_performers = stock_data.sort_values(by = 'changepercent',ascending = False)
    tp_names = list(top_performers['name'])
    tp_chpct = list(top_performers['changepercent'])
    tp_stkid = list(top_performers['code'])
    tp_spj = list(top_performers['trade'])
    tp_zrspj = list(top_performers['settlement'])
    total_count = len(top_performers)
    top_list = pd.DataFrame({'股票代码':tp_stkid,'股票名':tp_names,'收盘价':tp_spj,'昨日收盘价':tp_zrspj,'涨幅/%':tp_chpct},index = [ i for i in range(1,total_count+1)])
    top_10_performers = top_list[:50]
    return top_10_performers

# def get_top_10_droppers():
#     top_performers = stock_data.sort_values(by = 'changepercent')
#     tp_names = list(top_performers['name'])
#     tp_chpct = list(top_performers['changepercent'])
#     tp_stkid = list(top_performers['code'])
#     tp_spj = list(top_performers['trade'])
#     tp_zrspj = list(top_performers['settlement'])
#     total_count = len(top_performers)
#     # top_list = pd.DataFrame({'股票代码':tp_stkid,'股票名':tp_names,'涨幅/%':tp_chpct},index = [ i for i in range(1,total_count+1)])
#     top_list = pd.DataFrame({'股票代码':tp_stkid,'股票名':tp_names,'收盘价':tp_spj,'昨日收盘价':tp_zrspj,'涨幅/%':tp_chpct},index = [ i for i in range(1,total_count+1)])
#     top_10_performers = top_list[:20]
#     return top_10_performers

print("**********涨幅榜前10************")
print(get_top_10_perfomers())
# print("**********跌幅榜前10************")
# print(get_top_10_droppers())