import pymysql #导入数据操作的库
#连接数据库
db = pymysql.connect(host='180.76.115.84', user='root', passwd='admin123', db='legal_person', port=3306, charset='utf8')
#定义游标
cur =db.cursor()
#循环次数
count = 0
#定义数据表的字段名的初始值
sid=20  #给stid字段定义初始值
sscore=45  #给stscore 定义初始值
while count < 30:
    count += 1
    sname = 'SQname'+str(count)  #定义stname的格式
    sid+=1 #sid自增,不会重复
    stscore=sscore  #变量赋值
    stname=sname #变量赋值
    stid=sid #变量赋值
    values=(int(stid),str(stname),int(stscore)) #强制数据类型的匹配
    sql = """INSERT INTO sqstudent (stid,stname,stscore) values (%s,%s,%s)"""  #定义SQL语句
    cur.execute(sql,values)  #游标执行语句
    db.commit()  #数据提交
    print('条目'+str(count)+"已经创建成功")  #每一次插入后响应一个结果
print("数据已经插入完成")   #最后完成后响应一次
cur.close()  #游标关闭
db.close()  #数据库关闭




INSERT INTO admin_accide_inform(idcard,old_idcard,create_time,link_id,data_from,data_state,accide_time,accide_site,accide_types,cause_the_accide,
    number_deaths,seriou_injure_people,proper_damage,accide_summar)
VALUES('320100199003060412','320100900306041',NOW(),1234657891,'江宁区人员数据库',1,'2019-12-30 12:09:08','上海路与江东路交叉口','交通事故',
'前车经过路口急刹车，导致后车追尾，造成车辆侧翻',5,9,1000.2,'前车经过路口急刹车，导致后车追尾，造成车辆侧翻')