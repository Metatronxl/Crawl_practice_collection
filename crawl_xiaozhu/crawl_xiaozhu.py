#爬取网站为小猪北京短租网http://bj.xiaozhu.com/search-duanzufang-p1-0/

from bs4 import BeautifulSoup
import requests
import time

headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

def judgement_sex(class_name):
    if class_name == ['member_boy_ico']:
        return '男'
    else:
        return '女'

def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #通过使用Chrome的开发者选项,点击元素后,选择copy其中的selector就能得到
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_info(href)

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.content,'lxml')
    titles = soup.select('div.pho_info > h4')
    #note: 获取soup标签中的内容可以使用.text ,strip()可以去除空格间隙
    # for tmp in title:
    #     print(tmp.text.strip())
    addresses = soup.select('div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')

    for title,address,price,name,sex in zip(titles,addresses,prices,names,sexs):
        data={
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text().strip(),
            'name':name.get_text(),
            'sex':judgement_sex(sex.get("class"))
        }
        print(data)


if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)