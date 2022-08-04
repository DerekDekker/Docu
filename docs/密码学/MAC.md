from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives import hashes, hmac

Message authentication codes 消息验证码

可以确保信息的完整性 防篡改 认证性 防伪装


---------------------------------------------------- CMAC
CMAC 基于密码的消息认证码


# 加载密钥
c = cmac.CMAC(algorithms.AES(key))
# 添加信息
c.update(b"message to authenticate")
# 值计算
c.finalize()

# 认证 如果不正确 报错
c.verify(值)


---------------------------------------------------- HMAC
HMAC 基于散列的消息认证代码


# 加载密钥
h = hmac.HMAC(key, hashes.SHA256())
# 添加信息
h.update(b"message to hash")
# 值计算
h.finalize()
# 认证 如果不正确 报错
h.verify(值)


---------------------------------------------------- 方法
.copy()  # 复制实例

b''.hex()  # bytes 转 16进制






