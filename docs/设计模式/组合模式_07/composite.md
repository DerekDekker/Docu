from abc import ABCMeta, abstractmethod


"""
将对象组合成树形结构以表示 '部分|整体' 的成次结构(特别是递归结构) 使用户对单个对象和组合对象的使用具有一致性
可以一次性对某个节点做统一操作
"""
# 抽象主件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 点 叶子主件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'点{self.x, self.y}'

    def draw(self):
        print(str(self))


# 线 叶子主件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'线段 {self.p1} {self.p2}'

    def draw(self):
        print(str(self))


# 复杂节点
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []

        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print(f'------- 复合图形 -------')
        for g in self.children:
            g.draw()
        print(f'------- 复合图形 -------')


p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(6, 7))
l2 = Line(Point(1, 5), Point(2, 8))
pic1 = Picture([p1, l1, l2])

p2 = Point(4, 4)
l3 = Line(Point(1, 1), Point(0, 0))
pic2 = Picture([p2, l3])

pic = Picture([pic1, pic2])
pic.draw()

