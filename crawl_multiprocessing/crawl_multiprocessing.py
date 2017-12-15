import requests
import re
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def re_scraper(url):
    res = requests.get(url,headers=headers)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    for id,content,laugh,comment in zip(ids,contents,laughs,comments):
        info = {
            'id':id,
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        # return info
        # print(info)

def mutiProcessing(num,func,urls):
    pool = Pool(processes=num)
    pool.map(func,urls)

if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print("\nserial crawl :",end_1-start_1)

    start_3 = time.time()
    mutiProcessing(3,re_scraper,urls)
    end_3 = time.time()
    print("\n multiprocessing crawl:",end_3-start_3)

    # serial crawl : 29.88730216026306

    # multiprocessing crawl: 7.710344076156616