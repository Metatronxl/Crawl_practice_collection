# 爬取的网站为斗破苍穹小说网
# 本次demo主要是学习re模块的使用
# 其中用的最多的是(.*?)语法,可以匹配括号里的任何内容
# demo如下


import requests
import re
import time

headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

# def openFile():
#     try:
#         f = open(' /Users/xulei2/Desktop/doupo.txt','a+')
#     except

f = open('/Users/xulei2/Desktop/doupo.txt','a+')

def get_info(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'))
        for content in contents:
            f.write(content+'\n')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(num) for num in range(2,1665)]
    for url in urls:
        get_info(url)
        # time.sleep(1)
    f.close()