from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

----------------字段类型
Integer  整数
String(20)  字符串

----------------选项
primary_key=True  主键
nullable=False    可为空
index=True        索引
unique=True       唯一索引

----------------模型
class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))  # 多个域名

# 模型类 实例化
co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'imooc.com']
)