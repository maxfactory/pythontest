# www.zhongguantech.com
import requests
# kv = {'user-agent':'Mozilla/5.0'}
# url = 'https://www.amazon.cn/dp/B07X8FKFVG/ref=br_bsl_pdt-2?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-1&pf_rd_r=DHW9XGTVF4FVGFMV2842&pf_rd_r=DHW9XGTVF4FVGFMV2842&pf_rd_t=36701&pf_rd_p=2239dbbd-1fbb-4795-9d68-c227cd3c9261&pf_rd_p=2239dbbd-1fbb-4795-9d68-c227cd3c9261&pf_rd_i=desktop'
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
r = requests.get(url)
# r.encoding = 'utf-8'
# a = r.text
# print(a)
# encod = r.encoding
# encods = r.apparent_encoding
# print(encod)
# print(encods)
aa = r.request.headers
print(r.status_code)
# a = type(r)
print(aa)
# print(r.headers)
