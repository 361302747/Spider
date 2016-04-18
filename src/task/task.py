from apscheduler.schedulers.blocking import BlockingScheduler
from src.spider.h5shuo_spider import h5shuoSpider

#任务调度测试
def my_job():
    print('hello world')

sched = BlockingScheduler()
sched.add_job(h5shuoSpider, 'interval', seconds=5)
sched.start()