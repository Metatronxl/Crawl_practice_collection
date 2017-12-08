import requests
#get获取网址内容
def func1():
    content = requests.get("https://www.baidu.com")
    print(content.text)
 #加入请求头的requests
def func2():
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }

    content = requests.get("https://www.baidu.com",headers=headers)
    print(content.text)

#bug捕捉
def func3():
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
    content = requests.get("https://www.baidu.com",headers=headers)
    try:
        print(content)
    except ConnectionError:
        print("refuse connection")




if __name__ == '__main__':
    func1()