散列函

from cryptography.hazmat.primitives import hashes


SHA256 = hashes.Hash(hashes.SHA256())
SHA256.update(b"abc")
print(SHA256.finalize())  # bytes
print(SHA256.finalize().hex())  # 16进制


---------------------------------------------------- 算法
SHA-2
cryptography.hazmat.primitives.hashes.SHA224
cryptography.hazmat.primitives.hashes.SHA256
cryptography.hazmat.primitives.hashes.SHA384
cryptography.hazmat.primitives.hashes.SHA512
cryptography.hazmat.primitives.hashes.SHA512_224
cryptography.hazmat.primitives.hashes.SHA512_256

SHA-3
cryptography.hazmat.primitives.hashes.SHA3_224
cryptography.hazmat.primitives.hashes.SHA3_256
cryptography.hazmat.primitives.hashes.SHA3_384
cryptography.hazmat.primitives.hashes.SHA3_512
cryptography.hazmat.primitives.hashes.SHAKE128(长度int)
SHAKE128 任意长度 较长的长度不会增加安全性或抗碰撞性，而长度短于 128 位（16 字节）会降低安全性或抗碰撞性。
cryptography.hazmat.primitives.hashes.SHAKE256(长度int)
SHAKE256 任意长度 较长的长度不会增加安全性或抗碰撞性，而长度短于 256 位（32 字节）会降低安全性或抗碰撞性。

SHA-1
cryptography.hazmat.primitives.hashes.SHA1
已不安全

cryptography.hazmat.primitives.hashes.MD5
已不安全

















