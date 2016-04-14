import urllib.request

from lxml import etree
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import  hashlib
from src.entity.Item import iguoguoItem

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/h5doo')
# 创建DBSession类型:

DBSession = sessionmaker(bind=engine)

#爬取规则
set=set();
page=1
while page<1000:
    #定义初始url
    url = 'http://www.iguoguo.net/h5?action=ajaxPageLoad&toCat=0&yema='
    j=page
    url=url+str(j)
    try:
        urlop=urllib.request.urlopen(url,timeout=2)
        page = page + 1
        res=urlop.read().decode()
        tree = etree.HTML(res)
        session = DBSession()
        itemList=session.query(iguoguoItem).all()
        for item in itemList:
            set.add(item.url)
        liList=tree.xpath('//li[@class="depth0"]')
        print(url)
        for node in liList:
            newItem=iguoguoItem(name=str(node.xpath('div[1]/a/@title')[0]),url= str(node.xpath('div[1]/a/@href')[0]),cover=str(node.xpath('div[1]/a/img/@src')[0]),view=str(node.xpath('div[2]/span[2]/text()')[0]),create_date=str(node.xpath('div[2]/span[1]/text()')[0]))
            if(set.__contains__(newItem.url)):
                continue
            print(newItem.name)
            session.add(newItem)
            set.add(newItem.url)
            session.commit()
        id=tree.xpath('/html/body/div/@id')
        if('nomoreData' in id):
            break
    except Exception as e:
        print(e)
        continue

print('遍历结束')
session.close()

