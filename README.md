# Crawl_practice_collection
---
> just a pracetice collection for enhance my crawl skills. 
> if you like these codes, lt's my honour.

---
## requirements
> 详情查看requirements.txt

---
### demo1: 爬取小猪短租房的信息
> 工具：requests，BeautifulSoup4

> #Tips: 
> soup.select()配合上Chrome的selector（）选择器很好用！！！
### demo2: 爬取酷狗音乐Top500

---
### demo3：爬取网页小说（斗破苍穹）

> 工具：requests，Re模块
 
> 爬取的网站为斗破苍穹小说网,本次demo主要是学习re模块的使用,其中用的最多的是(.*?)语法,可以匹配括号里的任何内容

---
### demo4：爬取豆瓣图书Top250
> 工具：requests，lxml，xlwt

> 学习lxml的使用
```
注意点：
          infos = selector.xpath('//*[@id="content"]/div/div[1]/div/table')
          当table并没有包含tbody时，浏览器会自动补充tbody，而lxml没有这么做，所以会产生你的xpath没有找到的问题。
```
> csv的使用

> [xlwt 官网api文档](https://xlwt.readthedocs.io/en/latest/api.html)

---
### demo5：爬取pexles网站的图片

> 主要练习如何批量保存图片到本地

---
### demo6:爬取豆瓣音乐Top250的详细信息至MongoDB
- 工具：pymongo
> 练习xpath与正则的混合使用

> 练习mongoDB的使用

![mongoDB截图](https://github.com/Metatronxl/Crawl_practice_collection/blob/master/src_img/douban_music_top250.png);
