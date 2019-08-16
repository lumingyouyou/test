import requests
content = {"username":"niuhanyang","passwd":"aA123456"}
r = requests.post('http://api.nnzhp.cn/api/user/login',data=content)#post的参数调用用data
# print(r.url)#查看请求url --》http://api.nnzhp.cn/api/user/stu_info?stu_info=%E5%B0%8F%E9%BB%91
# print(r.status_code)#查看返回状态值--》200
print(r.text)#查看返回结果