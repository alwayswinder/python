'''
游民星空壁纸简易爬虫
'''
import urllib.request
import os

_path = os.getcwd() + '\\res\\image'

_url = 'https://www.gamersky.com/ent/'
_image_show_url = 'www.gamersky.com/showimage/id_gamersky.shtml?'
_image_test = 'https://img1.gamersky.com/image2019/11/20191115_lr_red_176_10/'\
	'gamersky_002origin_003_20191115203786E.jpg'
	

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


def find_image(page_url):
	'''查找图片链接'''
	html = get_html(page_url)
	pos_start = html.find(_image_show_url)
	addrs = []
	while pos_start!= -1:
		pos_img_start = pos_start+len(_image_show_url)
		pos_img_end = html.find('jpg', pos_img_start) + 3
		addrs.append(html[pos_img_start:pos_img_end])
		pos_start = html.find(_image_show_url, pos_start+len(_image_show_url))
	return addrs
	
	
def save_image(folder, img_addrs, page):
	'''保存图片到文件夹'''
	index = 0
	for addr in img_addrs:
		print(addr)
		html = get_html(addr, has_head_data = False, is_decode = False)
		with open(folder+'//' + str(page+1) + '_' + str(index) + '.jpg', 'wb') as imgfile:
			imgfile.write(html)
		index += 1


def get_page_max(page_url):
	'''获取最大页面数'''
	html = get_html(page_url) 
	a = html.rfind(page_url[0:-6] + '_') + len(page_url[0:-5])
	return int(html[a:a+1])


def download_image(url, folder = 'pachong_test_01'):
	'''图片爬虫接口'''
	folder = _path + '\\' + folder
	if not os.path.exists(folder):
		os.mkdir(folder)
		os.chdir(folder)
	page_max = get_page_max(url)
	for page in range(page_max):
		if page == 0:
			page_url = url
		else:
			page_url = url[0:-6] + '_' + str(page+1) + '.shtml'
		img_addrs = find_image(page_url)
		save_image(folder, img_addrs, page)
	
			
def gamersky_imag_auto_download():
	print('游民星空壁纸批量下载工具\n')
	images_id = input('请输入你要下载的壁纸主题id\n（例如https://www.gamersky.com/ent/201910/1227540'\
		'.shtml 时请输入 201910/1227540:\n')
	url = _url + images_id + '.shtml'
	print(url)
	download_image(url, images_id.replace('/', '_'))


gamersky_imag_auto_download()

