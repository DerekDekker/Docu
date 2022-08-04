from sqlalchemy import Column, String, Integer, BigInteger, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base


----------------基础
class 名称(Base):
    __tablename__ = 'city'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    名称 = relationship('关联类名', back_populates='名称')  # 关联

    __mapper_args__ = {'order_by', 字段}  # 排序 country_code.desc() 方法

    def __repr__(self):
        return f'{repr(self.date)}: 确诊{self.confirmed}例'


----------------类型
Integer  整型
BigInteger  大数型
String(100)  字符串

----------------参数
primary_key=False  主建
index=False  索引
autoincrement=False  自增长
unique=False  唯一索引
nullable=True|Flase  可为空
comment='内容'  注解
default=值  默认值

----------------外健
city_id = Column(Integer, ForeignKey('city.id'), comment='省')  # 外建



----------------扩展
created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')






