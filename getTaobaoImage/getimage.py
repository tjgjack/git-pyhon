# coding:utf-8
import urllib.request
import requests
import re
import json


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
#<img width="131" alt="清纯牛仔衣长发美女高清壁纸" src="http://t1.mmonly.cc/uploads/150729/8-150H91AJ4414.jpg">
def getNovelListUrl():
    html = urllib.request.urlopen('http://www.mmonly.cc/gqbz/mnbz/').read()
    html_page = html.decode('gb2312', 'ignore')
    # reg = r'<img width="131" alt=".*?" src="(.*?)"'
    reg = r'<img width="234" alt=".*?" src="(.*?)"'
    pattern = re.compile(reg)
    img_urls = re.findall(pattern,html_page)
    # print(html_page)
    print(img_urls)
    print(len(img_urls))
    n = 0
    for url in img_urls:
        n += 1
        urllib.request.urlretrieve(url,'F:\python_projects\getTaobaoImage\pics\{}.jpg'.format(n))

# getNovelListUrl()

def getsource(url):
    html = requests.get(url,headers=headers)
    page = html.text
    reg = r'<img src2="(.*?)"'
    reg = re.compile(reg)
    img_urls = re.findall(reg,page)
    print(img_urls)
    n = 0
    for url in img_urls:
        print('下载第{}张图片{}'.format(n,url))
        n += 1
        urllib.request.urlretrieve(url,'F:\python_projects\getTaobaoImage\pics\{}.jpg'.format(n))

# getsource('http://www.moko.cc/channels/post/23/1.html')

def gettaobaosource(url):
    html = requests.get(url,headers=headers)
    page = html.text
    reg = r'<img data-src="//(.*?)_50x50.jpg"'
    reg = re.compile(reg)
    url_list = re.findall(reg, page)
    print(url_list)
    dic = []
    n = 1
    for item in url_list:
        dic.append({'src':item})
        # dic[str(n)] = item
        n += 1
    print(dic)
    print(json.dumps(dic))
    print(len(dic))

gettaobaosource('https://item.taobao.com/item.htm?spm=a219r.lm874.14.240.324d0327duANFa&id=561707493365&ns=1&abbucket=5')