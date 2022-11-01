# MAC

消息验证码

可以确保信息的完整性 防篡改 认证性 防伪装 真实性


---
## HMAC

这是 `RFC 2104` 的实现, 基于哈希的消息身份验证码, 建议直接使用 HMAC

签名

```python
from cryptography.hazmat.primitives import hashes, hmac

# 加载密钥 SHA256可以更换
h = hmac.HMAC(key, hashes.SHA256())
# 添加信息
h.update(b"message to hash")
# 最终 签名
signature = h.finalize()
```

认证

```python
from cryptography.hazmat.primitives import hashes, hmac

# 加载密钥
h = hmac.HMAC(key, hashes.SHA256())
# 添加信息
h.update(b"message to hash")
# 认证 签名 如果不正确 抛异常
h.verify(b'签名')
```

---
## CMAC

方式 `RFC 4493` AES-128算法 , CMAC 基于密码的消息认证码

签名

```python
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

# 加载密钥
c = cmac.CMAC(algorithms.AES(key))
# 添加信息
c.update(b"message to authenticate")
# 最终 签名
signature = c.finalize()
```

认证

```python
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

# 加载密钥
c = cmac.CMAC(algorithms.AES(key))
# 添加信息
c.update(b"message to authenticate")
# 认证 签名 如果不正确 抛异常
c.verify(b'签名')
```

---
## Poly1305

方式 `RFC 7539`

签名

```python
from cryptography.hazmat.primitives import poly1305

# 加载密钥
p = poly1305.Poly1305(key)
# 添加信息
p.update(b"message to authenticate")
# 最终 签名
signature = p.finalize()
```

认证

```python
from cryptography.hazmat.primitives import poly1305

# 加载密钥
p = poly1305.Poly1305(key)
# 添加信息
p.update(b"message to authenticate")
# 认证 签名 如果不正确 抛异常
p.verify(b'签名')
```






