from abc import ABCMeta, abstractmethod


"""
多个维度组合
将一个事物的两个维度分离(不知道是否可以多个维度, 日后有机遇进行补充) 使用其都可以独立的变化
"""
# 形状类 维度 形状与颜色组合
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        # 画形状
        pass


# 颜色类 维度 形状与颜色组合
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        # 加颜色
        pass


# 长方形
class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        # 长方形逻辑
        self.color.paint(self)


# 圆形
class Circle(Shape):
    name = '圆形'

    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f'红色的{shape.name}')


class Green(Color):
    def paint(self, shape):
        print(f'绿色的{shape.name}')


# 客户端
shape = Rectangle(Red())
shape.draw()

shape2 = Circle(Green())
shape2.draw()
