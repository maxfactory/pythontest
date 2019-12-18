# def build_person(first_name,last_name):
# 	"""返回一个字典，其中包含有关一个人的信息"""
# 	person = {'first':first_name,'last':last_name}
# 	return person

# musician = build_person('jimi','hendrix')
# print(musician)
#------------------------------------------
# 修改函数，让其也能够存储年龄
def build_person(first_name,last_name,age=''):
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi','hendrix')
print(musician)
musician = build_person('jimi','hendrix',12)
print(musician)