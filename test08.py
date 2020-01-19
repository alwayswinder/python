'''
保存网页内容到文件
'''

import urllib.request
import os

path = os.getcwd() + '\\res'

url = 'https://www.baidu.com/'
'''
proxy_support = urllib.request.ProxyHandler({'http':'110.243.0.94:9999'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
'''
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()


with open(path + '\\whatmyip.txt', 'wb') as f:
	f.write(html)

print('end')

