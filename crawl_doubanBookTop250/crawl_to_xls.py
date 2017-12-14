from  lxml import etree
import requests
import csv
import time
import xlwt

# fp = open('doubanbook.csv','w+',newline='',encoding='utf-8')
# write = csv.writer(fp)
# write.writerow(('name','url','author','publisher','data','price','rate','commeent'))
headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
# for url in urls:
all_info_list=[]
def get_info(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//*[@id="content"]/div/div[1]/div/table')
#当table并没有包含tbody时，浏览器会自动补充tbody，而lxml没有这么做，所以会产生你的xpath没有找到的问题。
    for info in infos:
        name = info.xpath('tr/td[2]/div[1]/a/text()')[0].strip()
        url = info.xpath('tr/td[2]/div[1]/a/@href')[0].strip()
        comments = info.xpath('tr/td[2]/p[2]/span/text()')
        comment = comments[0] if len(comments) !=0 else "空"
        book_infos = info.xpath('tr/td[2]/p[1]/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('tr/td[2]/div[2]/span[2]/text()')[0].strip()
        # write.writerow((name,url,author,publisher,date,price,rate,comment))
        info_list = [name,url,author,publisher,date,price,rate,comment]
        all_info_list.append(info_list)
    time.sleep(1)


#sheet.write(r,c,data)
# r means rows
# c means cols

if __name__ == '__main__':
    urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_info(url)
    header = ['name','url','author','publisher','data','price','rate','commeent']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('book')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for list in all_info_list:
        j=0
        for data in list:
            sheet.write(i,j,data)
            j +=1
        i+=1
    book.save('douban_book_top250.xls')
    print("crawl success!\n")
