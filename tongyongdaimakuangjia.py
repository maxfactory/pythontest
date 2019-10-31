import requests

def getHTMLTest(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

if __name__ == "__main__":
	url = "http://112.29.169.2:8081/omc/"
	print(getHTMLTest(url))