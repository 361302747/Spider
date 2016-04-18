from apscheduler.schedulers.blocking import BlockingScheduler
from src.spider.h5shuo_spider import h5shuoSpider
from src.spider.h5share_spider import h5sharSpider
from src.spider.socialorz_spider import socialorzSpider
from src.spider.iguoguo_spider import iguoguoItem

#任务调度测试
def my_job():
    print('hello world')

sched = BlockingScheduler()
sched.add_job(h5sharSpider(), 'interval', seconds=5)
sched.start()