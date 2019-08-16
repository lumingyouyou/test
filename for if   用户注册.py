username=[]
password=[]
username1=str(input("请输入用户名："))
password1=int(input("请输入密码："))
cpassword1=int(input("请确认密码："))
for  count in range(4):
    if username.count(username1)>2 or password1!=cpassword1:#判断注册结果是否正常
        print("用户名或者密码错误，不能注册！")
        # username.append(username1)
        # password.append(password1)
        # print(username,password)
        continue
    else:
        username.append(username1)
        password.append(password1)
        print("注册成功",username,password)
        break
else:
    print("机会用完了！")

#


