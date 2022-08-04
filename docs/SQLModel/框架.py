from sqlmodel import SQLModel, create_engine


# 连接数据库
engine = create_engine("sqlite:///database.db")

# 单独放在一个函数里或文件里或if __name__ == "__main__":，只有运行的时候执行一次，防止在其他类里导入也被尝试创建数据库
# 创建数据库
SQLModel.metadata.create_all(engine)
    echo=True  # 打印SQL
    connect_args=connect_arg = {"check_same_thread": False}  # 不会在多个请求中共享相同的会话


