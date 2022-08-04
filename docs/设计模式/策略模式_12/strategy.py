from abc import ABCMeta, abstractmethod

"""
策略模式
行为模式

定义一系列算法 一个个封装起来 并使他们可以相互替换
本模式可独立于使用他的客户而变化
"""
# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


# 策略
class FastStratege(Strategy):
    def execute(self, data):
        print(f'用较快的策略处理{data}')


# 策略
class SlowStrategy(Strategy):
    def execute(self, data):
        print(f'用较慢的策略处理{data}')


# 上下文类 不想要用户知道的数据可以封装在这里
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        # 策略切换
        self.strategy = strategy

    def do_strategy(self):
        # 执行策略
        self.strategy.execute(self.data)


# 客户端
data = '[...]'
s1 = FastStratege()  # 较快的策略
s2 = SlowStrategy()  # 较慢的策略
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)  # 切换策略
context.do_strategy()
