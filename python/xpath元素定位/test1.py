"""selenium有几种定位元素的方法：
ID-唯一定位这个元素
classname,name,tagname
linktext,partial_link_text,css
xpath==>//h2[@属性="属性值"]

xpath表达式公式：
	//标签名[@属性="属性值"]

"""
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')


chrome_driver = r"C:\Program Files\Python38\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)

driver.get('https://blog.csdn.net/lufei051/article/details/78464538')

#selenium根据id来寻找元素
ele = driver.find_element_by_id("btnAttent")
print(ele.text)
# 根据class来寻找元素
ele1 = driver.find_element_by_class_name("title-article")
print(ele1.text)
# 通过xpath定位元素
xpath_code = '//h1[@class="title-article"]'
ele2 = driver.find_element_by_xpath(xpath_code)
print(ele2)



# 关闭浏览器
driver.quit()