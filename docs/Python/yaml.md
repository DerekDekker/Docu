# yaml

python 操作 yaml 文件

```shell
pip3 install pyyaml
```

---
## 读取

yaml会读取成为字典

```python
import yaml

with open('00.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
```

---
## 序列化

方法将 Python 对象序列化为 YAML 流

```python
import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

print(yaml.dump(users))
```

---
## 写入

将 YAML 流 写入文件

```python
with open('users.yaml', 'w') as f:

    data = yaml.dump(YAML流, f)
```

