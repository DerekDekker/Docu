from abc import ABCMeta, abstractmethod


"""
隐藏了对象创建的实现细节
每个类都有自己的工厂
需要的角色: 抽象工厂 具体工厂 抽象产品 具体产品
"""
# 抽象工厂
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 支付宝 抽象产品
class Alipay(Payment):
    def __init__(self, user_huabei=False):
        self.user_huabei = user_huabei  # 花呗

    def pay(self, money):
        if self.user_huabei:
            print(f'支付宝花呗付款{money}元')
        else:
            print(f'支付宝付款{money}元')


# 微信 抽象产品
class WechatPay(Payment):
    def pay(self, money):
        print(f'微信付款{money}元')


# 抽象类
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# 具体产品
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


# 具体产品
class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


# 具体工厂
class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(user_huabei=True)


pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)
