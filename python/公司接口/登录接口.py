import requests
from pprint import pprint

# header = {'Content-Type':'application/json;charset=UTF-8'}
res = requests.post('http://192.168.1.237:8005/datav/USER/LOGIN',json={
    "username":"admin",
    "password":"123456"
})
# print(res.status_code)
# print("*"*20)
retObj = res.json()
pprint(retObj,width=60)
# if retObj['REPCODE'] == 1:
# 	print('测试通过')
# print(res.cookies.get_dict())
# cookie = res.cookies.get_dict()
# session = cookie['SESSION']
print(res.cookies['SESSION'])
# url = 'http://192.168.1.237:8005/datav/ORG/ADDORG'
# jsons = {
#     "orgname":"中冠",
#     "domain":"zhongguan.com",
#     "verid":"5e6726460dd8be9540f4a68f",
#     "expiretime":"100",
#     "username":"max1",
#     "password":"123456"
# }
# res = requests.post(url,cookies=session,data=jsons)
# print(res.status_code)
# print("*"*20)
# retObj = res.json()
# pprint(retObj,width=60)