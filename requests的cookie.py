import requests
cookies = {"stu_id":"1","gold":"500"}
header='application/json;charset=UTF-8','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjE1NjU3NzY2MzE1NTAsInVpZCI6IjIwMTgxMjI5MTY1NjEyNDI2ZWY1NTcwYTI2Mzg5ZDIyIiwiaWF0IjoxNTY1NjkwMjMxNTUwLCJhY2NvdW50IjoibGl1ZGFoYW8iLCJwbGF0Zm9ybSI6InBjIn0.9RrcxCGhAQXZTfsDR17oLjkHQNdHMyRlEnZJAu7o2-Q'
r = requests.post('http://api.nnzhp.cn/api/user/gold_add',cookies=cookies)#post的参数调用用data
# print(r.url)#查看请求url --》http://api.nnzhp.cn/api/user/stu_info?stu_info=%E5%B0%8F%E9%BB%91
# print(r.status_code)#查看返回状态值--》200
print(r.text)#查看返回结果