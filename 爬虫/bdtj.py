# 百度提交关键字查询
import requests
keyword='python'
url = 'http://www.baidu.com/s'
try:
	kv = {'wd':keyword}
	r = requests.get(url,params=kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print("爬取失败")