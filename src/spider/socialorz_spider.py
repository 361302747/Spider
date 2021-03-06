import urllib.request
from lxml import etree
from src.entity.Item import socialorzItem,session

def socialorzSpider():
    #爬取规则
    myset=set();
    page=1
    while True:
        #定义初始url
        url = 'http://web.socialorz.com/item00'
        j=page
        url=url+str(j)+'.php'
        try:
            urlop=urllib.request.urlopen(url,timeout=2)
            res=urlop.read().decode()
            tree = etree.HTML(res)
            itemList=session.query(socialorzItem).all()
            for item in itemList:
                myset.add(item.url)
            liList=tree.xpath('//div[@class="h5_box"]')
            print('正在爬取第' + str(page) + '页--->')
            for node in liList:
                try:
                    newItem=socialorzItem(name=str(node.xpath('div[2]/h1/a/text()')[0]),keywords=str(node.xpath('//head/title/text()')[0]),url= str(node.xpath('div[2]/h1/a/@href')[0]),cover=str(node.xpath('div[1]/a/img/@src')[0]))
                    if(myset.__contains__(newItem.url)):
                        continue
                    print(newItem.name)
                    session.add(newItem)
                    myset.add(newItem.url)
                    session.commit()
                except Exception as e:
                    print(e)
                    continue
            id=tree.xpath('/html/body/text()')
            page = page + 1
            if('File not found' in id):
                break
        except Exception as e:
            if str(e).__contains__('404'):
                break
            continue

    print('遍历结束')
    session.close()
socialorzSpider()