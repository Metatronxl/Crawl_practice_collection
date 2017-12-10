#爬取网站为 http://www.kugou.com/yy/rank/home/1-8888.html
from bs4 import BeautifulSoup
import requests
import time

headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }


def get_web(url):
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.content,'lxml')
    ranks = soup.select('span.pc_temp_num > strong')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    urls = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')

    for rank,title,time,url in zip(ranks,titles,times,urls):
        data={
            'rank':rank.get_text().strip(),
            'title':title.get_text().strip(),
            'time':time.get_text().strip(),
            'url':title.get('href').strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(number) for number in range(1,24)]
    for url in urls:
        get_web(url)
        time.sleep(1)