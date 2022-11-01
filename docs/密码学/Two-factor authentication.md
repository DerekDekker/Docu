# Two-factor authentication

双重验证

```python
import time
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1
```

---
## 两步验证 计数器

这是 `RFC 4226` 的实现

```python
import os
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1

key = os.urandom(20)  # 至少是128位, 建议密钥为160位
hotp = HOTP(key, 6, SHA1())  # >= 6和<= 8

# 生成一次性密码值 第一个参数为次数
hotp_value = hotp.generate(0)  

# 认证是否正确 第二个参数为次数
hotp.verify(b'值', 0)
```

---
## 两步验证 时间

这是 `RFC 6238` 的实现

使用时间生成一次性密码值

```python
import os
import time
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1

key = os.urandom(20)  # 至少是128位, 建议密钥为160位
totp = TOTP(key, 8, SHA1(), 30)  # >= 6和<= 8

time_value = int(time.time())

# 生成一次性密码值
totp_value = totp.generate(time_value)

# 认证是否正确
totp.verify(totp_value, time_value)
```


---------------------------------------------------- 两步验证 时间间隔
# 密钥
key = os.urandom(20)

# 8代表长度 30代表时间间隔单位为秒
totp = TOTP(key, 8, SHA1(), 30)
# 当前时间
time_value = time.time()

# 返回一次性密码值
totp_value = totp.generate(time_value)

# 认证是否正确 totp_value一次性密码值
totp.verify(totp_value, time_value)

输出长度必须 >=6且<=8
key 每个用户的密钥。该值必须保密并且至少为 128位。建议密钥为 160 位。


---------------------------------------------------- 













