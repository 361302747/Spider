from urllib import request,parse
import json
from src.entity.Item import h5shareItem,session

def h5sharSpider():
    #爬取规则
    myset=set()
    page=1
    while True:
        j=page
        data = parse.urlencode([('screen',str(j))])
        itemList = session.query(h5shareItem).all()
        for h5share in itemList:
            myset.add(h5share.url)
        try:
            # 定义初始url
            req = request.Request('http://www.h5-share.com/h5share.php/Home/Index/JDOU_case_search/')
            response= request.urlopen(req, data=data.encode('utf-8'))
            res= response.read().decode()
            print('正在爬取第' + str(page) + '页--->')
            jsonObj=json.loads(res)
            if jsonObj["list"]== []:
                break
            for item in jsonObj["list"]:
                try:
                    newItem=h5shareItem(name=item["title"],url=item["url"],cover=item["img"],brief=item["description"])
                    if (myset.__contains__(newItem.url)):
                        continue
                    session.add(newItem)
                    myset.add(newItem.url)
                    print(newItem.name)
                    session.commit()
                except Exception as e:
                    print(e)
                    continue
            page = page + 1
        except Exception as e:
            print(e)
            continue

    print('遍历结束')
    session.close()
h5sharSpider()