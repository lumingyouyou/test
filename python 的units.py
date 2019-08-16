from urllib import request, parse
import json

# 下面是需要传递的参数
value = parse.urlencode({key1: value1, key2: value2})
# http请求头
headers = {key1: value1,
           key2: value2}
# 请求url
req = request.Request('url?%s' % value, headers=headers)  # 这样就能把参数带过去了
# 也可以用params关键字来传递这些参数

# 下面是获得响应
with request.urlopen(req) as f:
    Data = f.read()
    data = json.loads(Data)
    print(data)
