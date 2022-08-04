from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


---------------------------------------------------- 创建密钥
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)


---------------------------------------------------- 密钥加载
with open("path/to/key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )


password 可以是密码bytes类型


---------------------------------------------------- 密钥序列化
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)


print(pem.splitlines())


---------------------------------------------------- 密钥序列化 公钥
根据密钥序列化出对应的公钥



public_key = private_key.public_key()
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(pem.splitlines())



----------------------------------------------------  加密
message = b"encrypted data"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(ciphertext)


OAEP为 OAEP填充模式


---------------------------------------------------- 解密
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(plaintext)


OAEP为 OAEP填充模式


---------------------------------------------------- 填充模式
类
cryptography.hazmat.primitives.asymmetric.padding.OAEP
OAEP 被证明可以 抵御多种攻击类型。这是 RSA 加密推荐的填充算法。它不能与 RSA 签名一起使用。




