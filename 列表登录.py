#1、登录，要看判断用户名否在列表中
# 2、判断用户名和密码是否对应
username=['liu','dd']
password=['123','456']
uname=str(input("请输入用户名"))
pword=str(input("请输入密码"))
if  uname not in username  :
    # username[]==password:
    print("用户名不存在")
elif username.index(uname)==password.index(pword):
    print("登录成功")
else:
    print("登录失败")

