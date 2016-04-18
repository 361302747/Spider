from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.entity.Item import h5shareItem,h5shuoItem,socialorzItem,iguoguoItem,allItem

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/h5doo')
# 创建DBSession类型:

DBSession = sessionmaker(bind=engine)
set=set()
session = DBSession()
h5shareList = session.query(h5shareItem).all()
for h5share in h5shareList:
    set.add(h5share.url)
h5shuoList = session.query(h5shuoItem).all()
for h5share in h5shuoList:
    set.add(h5share.url)
socialorzList = session.query(socialorzItem).all()
for h5share in socialorzList:
    set.add(h5share.url)
iguoguoList = session.query(iguoguoItem).all()
for h5share in iguoguoList:
    set.add(h5share.url)
for h5share in h5shareList:
    if  set.__contains__(h5share.url):
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    set.add(h5share.url)
    session.commit()

for h5share in h5shuoList:
    if set.__contains__(h5share.url):
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    set.add(h5share.url)
    session.commit()

for h5share in socialorzList:
    if h5share.url not in set:
        if set.__contains__(h5share.url):
            continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    set.add(h5share.url)
    session.commit()

for h5share in iguoguoList:
    if h5share.url not in set:
        if set.__contains__(h5share.url):
            continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    set.add(h5share.url)
    session.commit()

session.close()