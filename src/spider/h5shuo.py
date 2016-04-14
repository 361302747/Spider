import urllib.request
from urllib import request,parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from src.entity.Item import h5shuoItem

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

    #获取数据库连接
    session = DBSession()
    itemList = session.query(h5shuoItem).all()
    for h5share in itemList:
        set.add(h5share.url)
    try:
        req = request.Request('http://api.h5shuo.com/apps?o=new&p='+str(page-1))
        page = page + 1
        response= request.urlopen(req)
        res= response.read().decode()
        jsonObj=json.loads(res)
        if str(jsonObj["err"]).__contains__('4'):
            break
        for item in jsonObj["data"]:
            newItem=h5shuoItem(name=item["name"],url=item["link"],cover=item["pic"],create_by=item["author"],create_date=item["update_time"])
            if (set.__contains__(newItem.url)):
                continue
            req2=request.Request(newItem)
            session.add(newItem)
            print(item.name)
            set.add(newItem.url)
            session.commit()

    except Exception as e:
        print(e)
        continue

print('遍历结束')
session.close()
