#1、写一个登陆的程序，最多登陆失败3次
#2、输入账号 密码，如果登录成功，程序结束，提示 欢迎 xx 登录，今天的日期是 xx
#3、登录失败，重新登陆
#3、要判断输入是否为空，什么也不输入，输入空格都算算空
#
# 1、用for控制次数
# 2、要有2个输入 用到input
#3、登录成功 用到break   和时间调用
# 4、登录失败，用到content
import datetime
# msg = "欢迎xxx登录，今天的日期是xxx"
username = 'xx'
date = datetime.datetime.today()
# msg = '欢迎'+username+'登录'+'今天的日期是'+date
msg2 = '欢迎%s登录，今天的日期是%s' % (username,date)
# msg3 = '欢迎%s登录' % username
count=3
while count:

    username=str(input("请输入用户名："))
    password=str(input("请输入密码："))
    if username=='yoyo' and password=='123456':
        print("登录成功，程序结束",msg2)
        break
    elif (username=='' and username==' ')or(password==''and password==' '):
        #     print('输入是否ded为空，什么也不输入，输入空格都算算空',count+1)
        print("登录失败，重新登陆",count,'次机会')
        continue
        # count = count - dwd1
    else:
        print("登录失败，重新登陆,您还有",count-1,'次机会')
    count-=1
else:
    print("机会用完了")








