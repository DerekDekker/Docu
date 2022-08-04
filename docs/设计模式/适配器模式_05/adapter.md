from abc import ABCMeta, abstractmethod


"""
将一个类的接口转换成客户希望的另一个接口
使原本由于接口不兼容而不能一起工作的那些类可以一起工作
"""
# 抽象类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print(f'支付宝付款{money}元')


class WechatPay(Payment):
    def pay(self, money):
        print(f'微信付款{money}元')


class BankPay:
    def cost(self, money):
        print(f'银联支付{money}')


class ApplePay:
    def cost(self, money):
        print(f'苹果支付{money}元')


# 类 适配器类
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


p = NewBankPay()
p.pay(100)


# 对象 适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(BankPay())
p.pay(100)
