from abc import ABCMeta, abstractmethod

"""
为其他对象提供一种代理以控制对这个对象的访问
种类: 
远程代理 为远程对象提供代理 待完善
虚代理 根据需要创建很大的对象 可以进行优化例如根据需求创建对象
保护代理 控制对原始对象的访问 用于对象有不同权限访问时 认证时 允许在访问一个对象时有一些附加的内部处理
"""
# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        # 获取
        pass

    @abstractmethod
    def set_content(self, content):
        # 设置
        pass


# 真实对象 原始对象 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        # 在创建对象时不占用资源 只有调用 get_content 时才占用资源
        f = open(filename, 'r')  # 打开文件 读
        self.content = f.read()  # 读取文件
        f.close()  # 关闭文件

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w')  # 打开文件 写
        f.write(content)
        f.close()


# 虚代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.set_content(content)


# 保护代理
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        if content == 1:
            # 可以做一些验证
            raise PermissionError('无写入权限')
        else:
            return self.subj.set_content(str(content))

# subj = RealSubject('test.txt')
# x = subj.get_content()
# print(x)

subj = ProtectedProxy('test.txt')
x = subj.set_content(331113)
print(x)
