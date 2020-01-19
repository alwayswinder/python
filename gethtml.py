'''
方便的网页内容获取接口
'''

import urllib.request


def get_html(url, has_head_data = True, is_decode = True):
	'''获取网页内容'''
	if has_head_data:
		data = {}
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'\
			' (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
		request = urllib.request.Request(url, data, head)
	else:
		request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	if is_decode:
		return response.read().decode('utf-8')
	else:
		return response.read()

def save_image(folder, img_addrs, page = 1):
	'''保存图片到文件夹'''
	index = 0
	for addr in img_addrs:
		print(addr)
		html = get_html(addr, has_head_data = False, is_decode = False)
		with open(folder+'//' + str(page+1) + '_' + str(index) + '.jpg', 'wb') as imgfile:
			imgfile.write(html)
		index += 1
