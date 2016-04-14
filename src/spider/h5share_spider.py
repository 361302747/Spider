import urllib.request
from urllib import request,parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from src.entity.Item import h5shareItem

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/h5doo')
# 创建DBSession类型:

DBSession = sessionmaker(bind=engine)

#爬取规则
set=set()
page=1
while True:
    #定义初始url
    j=page
    data = parse.urlencode([('screen',str(j))])
    session = DBSession()
    itemList = session.query(h5shareItem).all()
    for h5share in itemList:
        set.add(h5share.url)
    try:
        page = page + 1
        req = request.Request('http://www.h5-share.com/h5share.php/Home/Index/JDOU_case_search/')
        response= request.urlopen(req, data=data.encode('utf-8'))
        res= response.read().decode()
        print((res))
        jsonObj=json.loads(res)
        if jsonObj["list"]== []:
            break
        for item in jsonObj["list"]:
            newItem=h5shareItem(name=item["title"],url=item["url"],cover=item["img"],brief=item["description"])
            if (set.__contains__(newItem.url)):
                continue
            session.add(newItem)
            set.add(newItem.url)
            session.commit()

    except Exception as e:
        print(e)
        continue

print('遍历结束')
session.close()
