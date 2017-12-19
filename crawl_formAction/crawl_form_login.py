import requests
import json

headers={
    'Cookie':'_T_WM=fa46fe44449c4ea16c3fe320da571157; SSOLoginState=1513672121; ALF=1516264121; SCF=AmWx8JHQXGMEn_k5OvJhbYMx4NrhsURGnVBXFLPQ_1UlTqsgG_0CyhWH8gDmD8bY4Z1qS0woUuyA2kODhtv-j9I.; SUB=_2A253PL3pDeRhGeNP41UX9yfJwjiIHXVU3sOhrDV6PUNbktANLXCikW1NHetkTyNBWmRCJk-Kvm6InhlQ0u_DTZDM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFY4WgGImyiL.siwOYW.p695JpX5KMhUgL.Fo-p1hMcS0.f1KB2dJLoIXnLxKqLBK5LB.eLxKqLBK2L1K2LxKqLBKzL1h-LxKqL1-eLBo-LxKML1-2L1hBLxK-L1KnL1KnLxK-L1KnL1KnLxKML1-qLBoet; SUHB=0V5lVcQC_PklRw; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000174',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
}

f = open('weibo.txt','w+',encoding='utf-8')

def get_info(url,time,times):
    html = requests.get(url,headers=headers)
    json_data = json.loads(html.text)
    card_groups = json_data[0]['card_group']
    for card_group in card_groups:
        f.write(card_group['mblog']['text'].split(' ')[0]+'\n')
    next_cursor = json_data[0]['next_cursor']
    if time<=times:
        next_url = 'https://m.weibo.cn/feed/friends?version=v4&next_cursor={}&page=1'.format(str(next_cursor))
        print('已加载完第{}页内容'.format(time))
        time +=1
        get_info(next_url,time,times)


def get_weiboInfo(from_page,to_page):
    get_info('https://m.weibo.cn/feed/friends?version=v4',from_page,to_page)
    print('我的微博内容已经分析完成:)')

if __name__ == '__main__':
    get_info('https://m.weibo.cn/feed/friends?version=v4',1,50)
    print('我的微博内容已经分析完成:)')