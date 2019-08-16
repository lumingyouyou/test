import requests
import json
# cookies={'Cookie':'JSESSIONID=66F5C996F6BAE50ADA7884EE76583426; account=chengshu'}
header={'Content-Type':'application/json;charset=UTF-8','token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjE1NjU5NDYzOTA1NTgsInVpZCI6IjIwMTgxMjE0MTYzMTI4ODE3N2JiMzJiM2YwZDVkZWYzIiwiaWF0IjoxNTY1ODU5OTkwNTU4LCJhY2NvdW50IjoiY2hlbmdzaHUiLCJwbGF0Zm9ybSI6InBjIn0.g7avGWmxHAj94xnWdQPIa4vo0U1jBkXblvk26tKGot8'}
url='http://192.168.0.188:8006/#/task/selfaccess/post'
data={"uid":"","parentUid":"0","parentName":"","sort":0,"info":"","score":0,"name":"任务活动组织实施类1"}
r=requests.post(url,json=data,headers=header)
print(r.json())
