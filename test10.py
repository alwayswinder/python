'''
百度下图
'''
import urllib.request
import re
import requests
import os

from gethtml import save_image

_path = os.getcwd() + '\\res\\image'
_url = 'https://image.baidu.com/search/index'

def getDatas(keyword,pages):
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
        datas = requests.get(_url,params=i).json()
        datas = datas.get('data')
        for each in datas:
            addr_img = each.get('thumbURL')
            if addr_img != None:
                urls.append(addr_img)
    return urls
    
 
def getImg(): 
    key = input('input search key:\n')
    pages = input('input page number to download:\n')
    addrs_img=getDatas(key ,1)   
    folder = _path + '\\' + key + '_baidu'
    if not os.path.exists(folder):
        os.mkdir(folder) 
    save_image(folder, addrs_img)
 
if __name__ == '__main__':
    getImg()
