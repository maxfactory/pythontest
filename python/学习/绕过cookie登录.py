from selenium import webdriver
driver = webdriver.Chrome(r"D:\Program Files\Wolfram Research\Mathematica\11.3\SystemFiles\Components\WebUnit\Resources\DriverBinaries\ChromeDriver\Windows-x86-64\chromedriver.exe")
driver.get("http://106.15.228.37:3008/#/login")
cookies_data = driver.get_cookies()
print(cookies_data)