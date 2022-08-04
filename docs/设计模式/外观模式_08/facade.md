"""
外观模式定义了一个高层接口 这个接口使得这一子系统更加容易使用
不用调用子系统 而是封装一个高级的外观 来调用外观
"""


# 子系统
class CPU:
    def run(self):
        print('CPU开始运行')

    def stop(self):
        print('CPU停止运行')


# 子系统
class Disk:
    def run(self):
        print('硬盘开始工作')

    def stop(self):
        print('硬盘停止运行')


# 子系统
class Memory:
    def run(self):
        print('内存通电')

    def stop(self):
        print('内存断电')


# 外观 高级系统 通过高级接口的封装来完成子系统的调用
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()
computer.stop()
