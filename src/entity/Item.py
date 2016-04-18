# 导入:
from sqlalchemy import Column, String, create_engine,Integer,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    # 创建对象的基类:
    Base = declarative_base()
    #初始化数据库连接:
    engine=create_engine('mysql+mysqlconnector://root:1234@localhost:3306/h5doo')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
except Exception as e:
    print(e)

# 定义item对象:
class iguoguoItem(Base):
    # 表的名字:
    __tablename__ = 'iguoguo_spider'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(200))
    cover = Column(String(200))
    brief = Column(String(400))
    create_date = Column(TIMESTAMP)
    view = Column(String(20))
    keywords = Column(String(50))
    create_by = Column(String(40))

# 定义h5shareItem对象:
class h5shareItem(Base):
    # 表的名字:
    __tablename__ = 'h5share_spider'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(200))
    cover = Column(String(200))
    brief = Column(String(400))
    create_date = Column(TIMESTAMP)
    view = Column(String(20))
    keywords = Column(String(50))
    create_by = Column(String(40))

# 定义socialorz对象:
class socialorzItem(Base):
    # 表的名字:
    __tablename__ = 'socialorz_spider'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(200))
    cover = Column(String(200))
    brief = Column(String(400))
    create_date = Column(TIMESTAMP)
    view = Column(String(20))
    keywords = Column(String(50))
    create_by = Column(String(40))

# 定义socialorz对象:
class h5shuoItem(Base):
    # 表的名字:
    __tablename__ = 'h5shuo_spider'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(200))
    cover = Column(String(200))
    brief = Column(String(400))
    create_date = Column(TIMESTAMP)
    view = Column(String(20))
    keywords = Column(String(50))
    create_by = Column(String(40))
class allItem(Base):
    # 表的名字:
    __tablename__ = 'all_spider'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    url = Column(String(200))
    cover = Column(String(200))
    brief = Column(String(400))
    create_date=Column(TIMESTAMP)
    view=Column(String(20))
    keywords=Column(String(50))
    create_by=Column(String(40))