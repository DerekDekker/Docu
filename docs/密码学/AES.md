# AES

```python

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

```

---
## 基础

```python

# 密钥 256位
key = os.urandom(32)

# IV
iv = os.urandom(16)

# 加载密钥与加密模式
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))  # CBC 为 加密模式

```

## 加密

```python
# 加载加密
encryptor = cipher.encryptor()

# 加密
encryptor.update(b"明文") + encryptor.finalize()
```

## 解密

```python
# 加载解密
decryptor = cipher.decryptor()

# 解密
decryptor.update(b'秘文') + decryptor.finalize()
```


---
## 加密模式

现代的安全模式

### CBC

CBC（密码块链接）是一种用于分组密码的操作模式。它被认为在密码学上很强。

此模式需要填充 必须是随机字节, 它们不需要保密，每次加密时生成一个新的

```python
from cryptography.hazmat.primitives.ciphers.modes import CBC

```

### CTR

CTR（计数器）是分组密码的一种操作模式。它被认为在密码学上很强。它将分组密码转换为流密码。

IV字节不小于128. 必须是随机字节。它们不需要保密，每次加密时生成一个新的

```python
from cryptography.hazmat.primitives.ciphers.modes import CTR

```

### OFB

OFB（输出反馈）是分组密码的一种操作模式。它将分组密码转换为流密码。

必须是随机字节, 它们不需要保密，每次加密时生成一个新的

```python
from cryptography.hazmat.primitives.ciphers.modes import OFB

```

### CFB

CFB（密码反馈）是分组密码的一种操作模式。它将分组密码转换为流密码。

必须是随机字节, 它们不需要保密，每次加密时生成一个新的

```python
from cryptography.hazmat.primitives.ciphers.modes import CFB

```

### CFB8

CFB（密码反馈）是分组密码的一种操作模式。它将分组密码转换为流密码

必须是随机字节, 它们不需要保密，每次加密时生成一个新的

```python
from cryptography.hazmat.primitives.ciphers.modes import CFB8

```

---
## 加密算法

现代的安全算法

---
### AES

AES（高级加密标准）NIST标准化的分组密码。AES快速又加密强

cryptography.hazmat.primitives.ciphers.algorithms.AES
钥匙字节 128, 192, 256

---
### Camellia

Camellia 它被认为具有与AES相当的安全性和性能，但并未得到广泛研究或部署。

cryptography.hazmat.primitives.ciphers.algorithms.Camellia

钥匙字节 128, 192, 256




