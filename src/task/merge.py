from src.entity.Item import h5shareItem,h5shuoItem,socialorzItem,iguoguoItem,allItem,session


#合并多个库
myset=set()
h5shareList = session.query(h5shareItem).all()
for h5share in h5shareList:
    myset.add(h5share.url)
h5shuoList = session.query(h5shuoItem).all()
for h5share in h5shuoList:
    myset.add(h5share.url)
socialorzList = session.query(socialorzItem).all()
for h5share in socialorzList:
    myset.add(h5share.url)
iguoguoList = session.query(iguoguoItem).all()
for h5share in iguoguoList:
    myset.add(h5share.url)
for h5share in h5shareList:
    if  myset.__contains__(h5share.url):
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    myset.add(h5share.url)
    session.commit()

for h5share in h5shuoList:
    if myset.__contains__(h5share.url):
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    myset.add(h5share.url)
    session.commit()

for h5share in socialorzList:
    if h5share.url not in myset:
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    myset.add(h5share.url)
    session.commit()

for h5share in iguoguoList:
    if h5share.url not in myset:
        continue
    newItem = allItem(name=h5share.name, url=h5share.url,brief=h5share.brief,view=h5share.view, cover=h5share.cover, create_by=h5share.create_by,create_date=h5share.create_date)
    session.add(newItem)
    myset.add(h5share.url)
    session.commit()

session.close()