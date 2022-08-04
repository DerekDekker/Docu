from abc import ABCMeta, abstractmethod
from time import sleep


"""
模板模式
行为模式

场景
一次性实现一个算法的不变部分
各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
"""
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        # 创建一个窗口
        pass

    @abstractmethod
    def repaint(self):
        # 重新绘制窗口
        pass

    @abstractmethod
    def stop(self):
        # 关闭窗口
        pass

    # 模板方法 具体方法 整个框架
    # 到子类不变的操作
    # 有再多的窗口类像这样统一的大逻辑就不用在写了
    def run(self):
        # 框架
        self.start()  # 创建窗口
        while True:
            # 过一段时间需要重新绘制一次
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行')

    def stop(self):
        print('窗口结束运行')

    def repaint(self):
        print(self.msg)


# 客户端
MyWindow('Hello...').run()
