set =  dict()
set = { "init":"",
        "host":"",
        "user":"",
        "password":"",
        "database":""
        }

with open("option.config", "r")  as f:
	ret = eval(  f.read() )

for item in ret:
	set[item] = ret[item]

print(set.items())
