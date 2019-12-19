from collections import OrderedDict
# OrderedDict类的作用是创建字典并记录其中的键-值对的添加顺序
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")