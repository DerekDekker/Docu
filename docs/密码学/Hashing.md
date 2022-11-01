# Hashing

散列函

```python
from cryptography.hazmat.primitives import hashes

```

---
## 用法

```python
SHA256 = hashes.Hash(hashes.SHA256())  # SHA256 为 算法
SHA256.update(b'abc')

print(SHA256.finalize())  # bytes
print(SHA256.finalize().hex())  # 16进制
```

---
## 算法

###SHA-2

```python
from cryptography.hazmat.primitives.hashes import SHA224
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hashes import SHA384
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.primitives.hashes import SHA512_224
from cryptography.hazmat.primitives.hashes import SHA512_256
```

---
### SHA-3

```python
from cryptography.hazmat.primitives.hashes import SHA3_224
from cryptography.hazmat.primitives.hashes import SHA3_256
from cryptography.hazmat.primitives.hashes import SHA3_384
from cryptography.hazmat.primitives.hashes import SHA3_512
```

---
### SHAKE128 SHAKE256

#### SHAKE128

SHAKE128 任意长度 较长的长度不会增加安全性或抗碰撞性，而长度短于 128 位（16 字节）会降低安全性或抗碰撞性。

```python
from cryptography.hazmat.primitives.hashes import SHAKE128
SHAKE128(长度int)
```

#### SHAKE256

SHAKE256 任意长度 较长的长度不会增加安全性或抗碰撞性，而长度短于 256 位（32 字节）会降低安全性或抗碰撞性。

```python
from cryptography.hazmat.primitives.hashes import SHAKE256
SHAKE256(长度int)
```

---
### SHA-1

已不安全

```python
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.hashes import MD5
```

















