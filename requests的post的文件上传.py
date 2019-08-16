import requests
url = 'http://api.nnzhp.cn/api/file/file_upload'
files = {'file': open('d:\\Users\\ldh\\Desktop\\test.txt', 'rb')}
r = requests.post(url,files=files)
print(r.text)
