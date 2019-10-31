# zhongguantech
import requests
r = requests.get("http://112.29.169.2:8081/omc/")
# r.encoding = 'utf-8'
# a = r.text
# print(a)
# encod = r.encoding
# encods = r.apparent_encoding
# print(encod)
# print(encods)
print(r.status_code)
a = type(r)
print(a)
print(r.headers)