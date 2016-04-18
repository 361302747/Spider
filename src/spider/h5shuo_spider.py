from urllib import request
from lxml import etree
import json
from src.entity.Item import h5shuoItem,session

def h5shuoSpider():
    myset = set()
    #爬取规则
    page=1
    while True:
        itemList = session.query(h5shuoItem).all()
        for h5share in itemList:
            myset.add(h5share.url)
        print('正在爬取第' +str(page) + '页--->')
        try:
            # 定义初始url
            req = request.Request('http://api.h5shuo.com/apps?o=new&p='+str(page-1))
            page = page + 1
            response= request.urlopen(req)
            res= response.read().decode()
            jsonObj=json.loads(res)
            if str(jsonObj["err"]).__contains__('4'):
                break
            for item in jsonObj["data"]:
                newItem=h5shuoItem(name=item["name"],url=item["link"],cover=item["pic"],create_by=item["author"],create_date=item["update_time"])
                subreq=request.Request(newItem.url)
                subreq.add_header('User-Agent',
                               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
                subreq.add_header('Referer', 'http://www.h5shuo.com/?q=12169582980&from=show_rdr')
                try:
                    subresponse = request.urlopen(subreq,None,4)
                    responseurl=subresponse.geturl()
                    if 'h5shuo.com' not in responseurl:
                        newItem.__setattr__('url', responseurl)
                    else:
                        subres = subresponse.read().decode()
                        tree = etree.HTML(subres)
                        if str(tree.xpath('//body/iframe/@src')) != '[]':
                            baseUrl = str(tree.xpath('//body/iframe/@src')[0])
                            newItem.__setattr__('url', baseUrl)
                        elif str(tree.xpath('//base/@href'))!= '[]':
                            baseUrl = tree.xpath('//base/@href')[0]
                            newItem.__setattr__('url', baseUrl)
                except Exception as e:
                    print(e)
                    continue
                if (myset.__contains__(newItem.url)):
                    continue
                session.add(newItem)
                print(newItem.name)
                myset.add(newItem.url)
                session.commit()

        except Exception as e:
            print(e)
            continue

    print('遍历结束')
    session.close()
h5shuoSpider()