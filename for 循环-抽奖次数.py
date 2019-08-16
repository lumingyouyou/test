#1、猜数字游戏，最多猜7次
#2、循环7次
#3、输入一个数字，int
#4、判断是大于、小于、等于，如果是等于则跳出循环 break
#5、大于和小于，次数减1，并继续 content count-1
# import random
# number=random.randint(1,10)
# for j in range(3):
#     guess = int(input('请输入1到10的一个数字:'))
#     if guess>number:
#         print("大了",guess,number)
#         continue
#     elif guess<number:
#         print("小了",guess,number)
#         continue
#     else:
#         print('猜对了',guess,number)
#         break
# else:
#     print('错误次数已经用光')
#




# for x in range(7):  x可以是1-7

#     if  x==3: 当x=3 ,则跳出当前循环
#         continue
#     elif x==5: 当x=5,则结束当前循环
#         break
#     print(x)


for x in range(5):
    if x==2:
        x=x+1
    print(x)












