'''
游民星空壁纸简易爬虫
'''
import os

from gethtml import get_html
from gethtml import save_image

_path = os.getcwd() + '\\res\\image'

_url = 'https://www.gamersky.com/ent/'
_image_show_url = 'www.gamersky.com/showimage/id_gamersky.shtml?'
_image_test = 'https://img1.gamersky.com/image2019/11/20191115_lr_red_176_10/'\
	'gamersky_002origin_003_20191115203786E.jpg'
	

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



if __name__ == '__main__':
    gamersky_imag_auto_download()

