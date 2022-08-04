"""
责任链模式
行为模式

多个对象都有机会处理请求 将这些对象连成一条链 并沿着这条链传递该请求 直到有一个对象处理它为止
可以只有一个链最终处理 也可以每个链都处理一遍
"""
from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        # 请假处理
        pass


# 总经理
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print(f'总经理批假 {day} 天')
        else:
            print('你还是辞职吧')


# 部门经理
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print(f'部门经理批假 {day} 天')
        else:
            print('部门经理职权不足')
            self.next.handle_leave(day)


# 项目主管
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print(f'项目主管准假 {day} 天')
        else:
            print('项目主管职权不足')
            self.next.handle_leave(day)


# 客户端
day = 7  # 请假天数
h = ProjectDirector()
h.handle_leave(day)

