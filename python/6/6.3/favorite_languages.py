# favorite_languages = {
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'ruby',
# 	'phil':'python',
# }

# for name,language in favorite_languages.items():
# 	print(name.title() + "'s favorite language is " + language.title() + ".")

# 像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，指出其喜欢的放言。
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print("Hi " + name.title() + ",I see you favorite language is " +
			favorite_languages[name].title() + "!")