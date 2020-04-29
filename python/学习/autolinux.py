import time

import paramiko

#创建sshclient对象
ssh=paramiko.SSHClient()
#第一次登录linxu 默认接受公钥
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程机器-用户名，ip ，端口，密码
ssh.connect('180.76.115.84',40420,'qiang','admin123')

#大量重复的操作，比如部署环境，操作多态机器，
#或者有些环境，需要反复卸载反复安装

#执行linxu命令
cmd1='mkdir testdir'
cmd2='cd testdir'
cmd3='touch mem.txt'
cmd4='free -m >> mem.txt'
cmds=[cmd1,cmd2,cmd3,cmd4]
cmds=';'.join(cmds)

#每次执行exec_command相当于重新打开一个命令行
for i in range(10):
    ssh.exec_command(cmd4)
    time.sleep(1)#每隔1s监控1次