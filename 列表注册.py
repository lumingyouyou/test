#注册
# 1、用户名不能大于2次
# 2、密码和确认密码要重复
# 3、可以注册有3次机会，1次注册成功则结束任务。并保留数据

username=[]
password=[]
username1=str(input("请输入用户名："))
password1=int(input("请输入密码："))
cpassword1=int(input("请确认密码："))
for  count in range(4):
    if username.count(username1)<2 and  password1==cpassword1:#判断注册结果是否正常

        username.append(username1)
        password.append(password1)
        print("注册成功",username,password)
        break
    elif username.count(username1)>2 or  password1==cpassword1:
        print("用户名或者密码错误，不能注册！")
        continue
    else:
        print("不能注册！")
else:
    print("机会用完了！")

