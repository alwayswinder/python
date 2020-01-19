'''
有道翻译
'''
import urllib.request
import urllib.parse
import json

str_t = ''
btrans = True

while btrans:
	str_t = input('请输入你要翻译的内容:\n')
	
	if str_t == '':
		print('你没有输入任何字符')
		continue
		
	if str_t == 'quit':
		btrans = False
		continue
		 
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	data = {}

	data['i'] = str_t
	data['from'] = 'AUTO'
	data['to']  = 'AUTO'
	data['smartresult']  = 'dict'
	data['client'] = 'fanyideskweb'
	data['salt'] = '1579244932770'
	data['sign'] = '38895fbc82a9d74d821f3a6c4e689448'
	data['ts'] = '1579244932770'
	data['bv'] = 'bc250de095a39eeec212da07435b6924'
	data['doctype'] = 'json'
	data['version'] = '2.1'
	data['keyfrom'] = 'fanyi.web'
	data['action'] = 'FY_BY_CLICKBUTTION'

	data = urllib.parse.urlencode(data).encode('utf-8')

	request = urllib.request.Request(url, data)
	response = urllib.request.urlopen(request)
	res = response.read().decode('utf-8')
	
	res = json.loads(res)
	
	print(res['translateResult'][0][0]['tgt'])
	
