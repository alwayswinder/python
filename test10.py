'''
正则表达式在网页内容查找中的应用
'''
import re
import os
import urllib.request

from gethtml import get_html
from gethtml import save_image

_url = 'https://image.baidu.com/search/index'
_path = os.getcwd() + '\\res\\image'	
	
def get_imgs(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1526377465547': ''
                  })
    urls = []
    for i in params:
        data = urllib.request.Request(_url,params=i).json().get('data')
        urls.append(data.get('thumbURL'))
        
    save_image(_path, urls)


get_imgs('', 1)
