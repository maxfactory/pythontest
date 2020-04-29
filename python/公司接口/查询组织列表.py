import requests

def login():
	login_url = 'http://192.168.1.237:8005/datav/USER/LOGIN'
	body = {
    "username":"admin",
    "password":"123456"}
    try:
    	res = requests.post(url=login_url,data=body)
    	cookies = res.cookies

    	cookie = requests.utils.dict_from_cookiejar(cookies)
    	return cookie
    except Exception as err:
    	print('获取cookie失败：\n{0}'.format(err))