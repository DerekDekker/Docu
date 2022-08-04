from sqlmodel import Field, Session, SQLModel, create_engine, select


session = Session(bind=engine)


# ---------------------------------- 根据ID查询
获取一条数据
session.get(SQLModel类, 1)

# ---------------------------------- 查询全部数据
# 返回可迭代对象
with Session(engine) as session:
    statement = select(SQLModel类)
    # 执行
    # 获取到一个可迭代到对象
    results = session.exec(statement)

# ---------------------------------- 筛选
# 返回可迭代对象
statement = select(SQLModel类).where(SQLModel类.属性 == '值')
results = session.exec(statement)


# 筛选方式
.where(SQLModel类.属性 == '值')
.where(SQLModel类.属性 == '值', SQLModel类.属性 == '值')
.where(SQLModel类.属性 == '值').where(SQLModel类.属性 == '值')

# or 满足两个条件的都会返回
.where(or_(SQLModel类.属性 == '值', SQLModel类.属性 == '值'))

# 可以处理特殊类型 不使用此方式会错误提示但不影响使用
.where(col(SQLModel类.属性) == '值')

# 返回前3条数据
.limit(3)

# 偏移量 返回3条后的全部数据
.offset(3)

# 运算符
==
!=
<
>
>=
<=

# ----------------------------------

# 将可迭代对象返回成一个列表
heroes = results.all()
# 将可迭代对象返回成一个条数据
heroes = results.first()
# 返回一条数据，如果不是将报错
heroes = results.one()
#

# ---------------------------------- 多对多查询
statement = select(外键SQLModel类, 主键SQLModel类).where(外键SQLModel类.外键ID == 主键SQLModel类.主键ID)
返回可迭代对象
results = session.exec(statement)

只要外键SQLModel类数据 但 主键SQLModel类 进行筛选
statement = select(外键SQLModel类).where(外键SQLModel类.外键ID == 主键SQLModel类.主键ID)

写法二
自动链接
statement = select(外键SQLModel类, 主键SQLModel类).join(主键SQLModel类)
results = session.exec(statement)

.join(主键SQLModel类)
    isouter=False   # 是否 显示没有连接的数据

# ----------------------------------


# ----------------------------------

