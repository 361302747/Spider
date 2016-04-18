# Spider readme

####  项目说明：一个简单的定向爬虫
* entity/item.py 每个网站对应的实体类，以及在数据库中的表名在此声明
* spider/ 每个网站对应爬虫，在此编写
* task/merge.py 合并所有表中的数据，暂时需要手动添加代码
* task/task.py 定义定时任务的调度等
* config.conf 暂未使用

#### 环境配置：
* python版本：3.5.1
* orm框架:sqlalchemy  安装命令：`pip install sqlalchemy`
* 任务调度：apscheduler 安装命令:`pip install apscheduler(暂未完成)`

#### SVN地址：
`https://182.254.166.59/svn/h5doo-spider/`
    
#### 添加新爬虫说明：
* 在item中添加实体类
* 新建spide.py，引入`from src.entity.Item import xxxxItem,session`
* 编写爬取规则
* 添加定时任务