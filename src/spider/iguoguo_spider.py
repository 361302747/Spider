import urllib.request
from lxml import etree
from src.entity.Item import iguoguoItem,session

def iguoguoSpider():
    #爬取规则
    myset=set();
    page=1
    while page<1000:
        #定义初始url
        url = 'http://www.iguoguo.net/h5?action=ajaxPageLoad&toCat=0&yema='
        j=page
        url=url+str(j)
        try:
            urlop=urllib.request.urlopen(url,timeout=2)
            res=urlop.read().decode()
            tree = etree.HTML(res)
            itemList=session.query(iguoguoItem).all()
            for item in itemList:
                myset.add(item.url)
            liList=tree.xpath('//li[@class="depth0"]')
            print('正在爬取第' + str(page) + '页--->'+url)
            for node in liList:
                try:
                    newItem=iguoguoItem(name=str(node.xpath('div[1]/a/@title')[0]),url= str(node.xpath('div[1]/a/@href')[0]),cover=str(node.xpath('div[1]/a/img/@src')[0]),view=str(node.xpath('div[2]/span[2]/text()')[0]),create_date=str(node.xpath('div[2]/span[1]/text()')[0]))
                    if(myset.__contains__(newItem.url)):
                        continue
                    print(newItem.name)
                    session.add(newItem)
                    myset.add(newItem.url)
                    session.commit()
                except Exception as e:
                    print(e)
                    continue
            id=tree.xpath('/html/body/div/@id')
            page = page + 1
            if('nomoreData' in id):
                break
        except Exception as e:
            print(e)
            continue

    print('遍历结束')
    session.close()
iguoguoSpider()
