import urllib.request

from lxml import etree
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import  hashlib
from src.entity.Item import socialorzItem

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/h5doo')
# 创建DBSession类型:

DBSession = sessionmaker(bind=engine)

#爬取规则
set=set();
page=1
while True:
    #定义初始url
    url = 'http://web.socialorz.com/item00'
    j=page
    url=url+str(j)+'.php'
    try:
        urlop=urllib.request.urlopen(url,timeout=2)
        page = page + 1
        res=urlop.read().decode()
        tree = etree.HTML(res)
        session = DBSession()
        itemList=session.query(socialorzItem).all()
        for item in itemList:
            set.add(item.url)
        liList=tree.xpath('//div[@class="h5_box"]')
        print(url)
        for node in liList:
            newItem=socialorzItem(name=str(node.xpath('div[2]/h1/a/text()')[0]),keywords=str(node.xpath('//head/title/text()')[0]),url= str(node.xpath('div[2]/h1/a/@href')[0]),cover=str(node.xpath('div[1]/a/img/@src')[0]))
            if(set.__contains__(newItem.url)):
                continue
            print(newItem.name)
            session.add(newItem)
            set.add(newItem.url)
            session.commit()
        id=tree.xpath('/html/body/text()')
        if('File not found' in id):
            break
    except Exception as e:
        if str(e).__contains__('404'):
            break
        continue

print('遍历结束')
session.close()

