import pymongo
import datetime
post = {"author": "Mike",

        "text": "My first blog post!",

         "tags": ["mongodb", "python", "pymongo"],

         "date": datetime.datetime.utcnow()}

# 指定Monogo数据库为本地数据库,如果是远程库,则为(ip,port)
client = pymongo.MongoClient('localhost',27017)
# 新建一个数据库
mydb = client['mydb']
#新建一个collection
test = mydb['test']
#插入一行数据
test.insert_one({'name':'Jan','sex':'male','grade':89})
#批量插入
test.insert(post)
#获取一行数据
print(test.find_one())
#获取特定数据(批量)
print(test.find({'author':'Mike'}))
