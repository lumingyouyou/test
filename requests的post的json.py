import requests
import json
cookies={'JSESSIONID':'251A4821BCB595FA2C0CB94848882E10', 'account':'liudahao'}
header='application/json;charset=UTF-8','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjE1NjU3NzY2MzE1NTAsInVpZCI6IjIwMTgxMjI5MTY1NjEyNDI2ZWY1NTcwYTI2Mzg5ZDIyIiwiaWF0IjoxNTY1NjkwMjMxNTUwLCJhY2NvdW50IjoibGl1ZGFoYW8iLCJwbGF0Zm9ybSI6InBjIn0.9RrcxCGhAQXZTfsDR17oLjkHQNdHMyRlEnZJAu7o2-Q'
url='http://192.168.0.188:8006/access/tk/post'
data={"uid":"","parentUid":"0","parentName":"","sort":0,"info":"","score":0,"name":"任务活动组织实施类1"}
r=requests.post(url,data=json.dumps(data),cookies=cookies) #在一些post请求中，还需要用到headers部分，此处未加，在下文中会说到
print(r.text)