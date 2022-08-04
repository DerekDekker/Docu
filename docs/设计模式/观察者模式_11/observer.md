"""
观察者模式
行为模式

设计时设计成可以取消订阅
当发布者状态改变时 所有依赖他的订阅者都得到通知并被自动更新
观察者模式又称 发布-订阅 模式

"""
from abc import ABCMeta, abstractmethod


# 抽象 观察者 订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):  # notice 是 Notice 的一个对象
        # 发布者状态发生改变时 更新
        pass


# 抽象 发布者 主题 订阅关系不能写死
class Notice:
    def __init__(self):
        self.observers = []  # 存储所有订阅者

    def attach(self, obs):
        # 订阅
        self.observers.append(obs)

    def detach(self, obs):
        # 取消订阅
        self.observers.remove(obs)

    def notify(self):
        # 发布
        for obs in self.observers:
            obs.update(self)


# 具体发布者 主题
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company__info = company_info

    @property
    def company_info(self):
        return self.__company__info

    @company_info.setter
    def company_info(self, info):
        self.__company__info = info
        self.notify()


# 具体 观察者 订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice('初始公司信息')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = 'HiHiHi'
print(s1.company_info)