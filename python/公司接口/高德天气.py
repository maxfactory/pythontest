import requests

# weather_url = "https://restapi.amap.com/v3/weather/weatherInfo?"
weather_url = "https://restapi.amap.com/v3/weather/weatherInfo?city=320100&key=7f97132f2cd6a6a9d78e0f6ce64fda30"
body = {
	'city':'320100',
	'key':'7f97132f2cd6a6a9d78e0f6ce64fda30',
}
res = requests.get(url=weather_url)
retObj = res.json()
retObj = dict(retObj)
print(retObj['lives'])

