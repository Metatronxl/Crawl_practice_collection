import requests
from lxml import etree
import re
import pymongo
import time

#create database
client = pymongo.MongoClient('localhost',27017)
music_db = client['music']
musictop = music_db['musictop']

headers ={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def get_url_music(url):
    html  = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/@href')
    for href in music_hrefs:
        get_detail_musicInfo(href)

def get_detail_musicInfo(url):

    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    #注:下面的author获取有时候会错误,因为网站的作者位置显示不固定
    #author = selector.xpath('//*[@id="info"]/span[1]/span/a/text()')[0]
    author = re.findall('表演者:.*?>(.*?)</a>',html.text,re.S)[0]
    #有可能存在没有style的情况,所以这里不能用【0】
    #    style = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',html.text,re.S)[0]
    # re.S 用于跨行匹配
    style = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(style) == 0:
        style = '未知'
    else:
        style = style[0].strip()

    time = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />',html.text,re.S)[0].strip()
    publishers = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(publishers) == 0:
        publishers = '未知'
    else:
        publishers = publishers[0].strip()

    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]

    info ={
        'name':name,
        'author':author,
        'style':style,
        'time':time,
        'publisher':publishers,
        'score':score
    }

    musictop.insert_one(info)
    print('成功插入:',url,"的数据\n")

if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_url_music(url)
        time.sleep(2)
