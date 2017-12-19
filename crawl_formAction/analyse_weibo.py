import jieba.analyse



def jieba_analyse():
    path = 'weibo.txt'
    fp = open(path,'r',encoding='utf-8')
    fp2 = open('result.txt','w+',encoding='utf-8')
    content = fp.read()
    try:
        jieba.analyse.set_stop_words('useless_words.txt')
        tags = jieba.analyse.extract_tags(content,topK=100,withWeight=True)
        for item in tags:
            res = item[0]+'\t'+str(int(item[1]*1000))+'\n'
            # print(res)
            fp2.write(res)
    finally:
        fp.close()
        fp2.close()


if __name__ == '__main__':
    jieba_analyse()