import requests
url = 'https://www.amazon.cn/dp/B07GJBBGHG?ref_=Oct_DotdV2_PC_3_GS_DOTD_5b23caaa&pf_rd_r=25TZ8WACKGXRF0KHWTS4&pf_rd_p=8c48638a-3752-448a-8685-5a17153fb132&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2'
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("爬取失败")