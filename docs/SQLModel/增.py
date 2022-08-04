from sqlmodel import Session

session = Session(bind=engine)

# 添加数据
名称 = SQLModel类(字段=值, 字段=值)

# 为外键添加数据
名称 = SQLModel类(字段=值, 外键字段=SQLModel实例.主键属性)

# 增加 添加多个(要么全部成功要么全部失败)
# 添加也可以使用 with 语句
session.add(名称)
session.add(名称)
session.add(名称)

# 提交
session.commit()

# 关闭 释放资源
session.close()

# 刷新数据 刷新后 object 将有数据
session.refresh(object)

----------------------------------改
名称.属性 = 值

# 添加或更新 外键关系
名称.外键属性 = 主键SQLModel实体.主键ID

# 移除外键关系
名称.外键属性 = None

session.add(名称)
session.commit()

----------------------------------删
session.delete(名称)
session.commit()

----------------------------------知识点
# 数据提交后 访问 名称.属性 会自动在数据库中刷新数据

