import requests

from pprint import pprint

# 获取课程列表
res = requests.get('http://www.baidu.com')
list1 = res.json()['retlist']


# 添加一个课程
res = requests.post('http://xxxxx',
	data={
	'action':'add_course',
	'data':'''
	{
	"name":"初中化学",
	"desc":"初中化学课程"，
	"display_idx":"4"
	}'''
	})

retObj = res.json()
pprint(retObj,width=30)
if retObj['retcode'] == 0:
	print('检查点==>返回结果retcode为0，检查通过')
else:
	print('检查点==>返回结果retcode不为0，检查不通过')



# 获取课程列表
res = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course')
res = requests.get('http://www.baidu.com')
list2 = res.json()['retlist']
# print(res.status_code)
# print(res.json(),width=30)
# 取出多出来的一门课程对象
newcourse = None

for one in list2:
	if one not in list1:
		newcourse = one
		break

# 检查是否是刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='你好4'
assert newcourse['desc']=='你好'
assert newcourse['display_idx']==1

print('\n****test case pass****')