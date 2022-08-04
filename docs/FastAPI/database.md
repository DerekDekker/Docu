# 数据库配置
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DSTSBSSE_URL = 'sqlite:///./coronavirus.sqlite3'
# SQLALCHEMY_DSTSBSSE_URL = 'postgresql://用户名:密码@地址:端口/数据库名'


# 数据库引擎
engine = create_engine(
    SQLALCHEMY_DSTSBSSE_URL, encoding='utf-8', echo=True, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

# 创建基本的映射类
Base = declarative_base(bind=engine, name='Base')







