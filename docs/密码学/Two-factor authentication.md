Two-factor authentication 双重验证

import time
from cryptography.hazmat.primitives.twofactor.hotp import HOTP
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1


---------------------------------------------------- 两步验证 计数器
# 密钥
key = os.urandom(20)

# 6代表长度
hotp = HOTP(key, 6, SHA1())

# 返回一次性密码值 1用于生成一次性密码的计数器值
hotp_value = hotp.generate(1)

# 认证是否正确 hotp_value一次性密码值 1用于生成一次性密码的计数器值
hotp2.verify(hotp_value, 1)


输出长度必须 >=6且<=8
key 每个用户的密钥。该值必须保密并且至少为 128位。建议密钥为 160 位。


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













