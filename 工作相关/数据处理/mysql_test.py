import pymysql

#使用cursor()方法创建一个游标对象

##################
###    查询    ###
##################
# db = pymysql.connect(host='180.76.115.84', user='root', passwd='admin123', db='legal_person', port=3306, charset='utf8')
# cursor = db.cursor()
#使用execute()方法执行SQL语句
# cursor.execute("SELECT * FROM admin_accide_inform")
# #使用fetall()获取全部数据
# data = cursor.fetchall()
# #打印获取到的数据
# print(data)
# #关闭游标和数据库的连接
######################
config = {
	'host':'180.76.115.84', 
	'user':'root',
	'passwd':'admin123',
	'db':'legal_person',
	'port':3306, 
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO admin_accide_inform(idcard,old_idcard,data_from) VALUES(%s,%s,%s)"
for i in range(10):
	cursor.execute(sql,("320106199801020412","320106980102041",'测试'+str(i)))  
db.commit()  #提交数据

cursor.close()
db.close()
