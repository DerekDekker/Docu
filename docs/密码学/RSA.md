## RSA

目前1024及以下被认为是可破解的, 而2048或4096是新密钥的合理默认密钥大小

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
```

---
## 创建密钥

```python
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,  # 不变
    key_size=2048,  # 位数
)

```

---
## 密钥加载

使用本地密钥

```python
from cryptography.hazmat.primitives import serialization

with open("path/to/key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # 密码 可以为空 bytes 类型
    )
```

---
## 密钥序列化

### 无加密序列化 私钥

```python
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(pem.splitlines())
```

### 加密序列化 私钥

```python
from cryptography.hazmat.primitives import serialization

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')  # 加密
)

print(pem.splitlines())
```

### 序列化 公钥

```python
from cryptography.hazmat.primitives import serialization

public_key = private_key.public_key()  # 公钥
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem.splitlines())
```

---
## 加密

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

message = b'encrypted data'  # 要加密的内容
public_key = private_key.public_key()  // 公钥
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
    )
)

print(ciphertext)
```


OAEP为 OAEP填充模式

---
## 解密

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
    )
)

print(plaintext)
```


OAEP为 OAEP填充模式

---
## 填充模式

OAEP 被证明可以 抵御多种攻击类型。这是 RSA 加密推荐的填充算法。它不能与 RSA 签名一起使用。




