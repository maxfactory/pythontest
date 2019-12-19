"""
调用 open()时提供两个实参。第一个实参是要打开的文件的名称；
第二个实参('w') 告诉Python，我们要以写入模式打开这个文件；
打开文件时，可指定模式：
	读取模式：('r')
	写入模式：('w')
	附加模式：('a')
	读取和写入文件的模式：('r+')
如果活力模式实参，Python将以默认的只读模式打开文件。
"""
# filename = 'programming.txt'
# with open(filename,'w') as file_object:
# 	file_object.write("I love programming.")

#----------------------------------------------

#写入多行
filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love create new games.\n")