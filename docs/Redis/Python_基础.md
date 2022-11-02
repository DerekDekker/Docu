# Redis 基础

Redis 的 python 操作

```shell
pip3 install redis
```

键可以为 名称:名称:名称

---
## 连接

```python
r = redis.StrictRedis(host='IP', port=6379, db=0, password='密码')
```

??? 参数

    decode_responses=False  是否取出来的是字符串

### 连接池

避免每次建立、释放连接的开销

```python
pool = redis.ConnectionPool(host='IP', port=6379, db=0, password='密码', decode_responses=True)
r = redis.Redis(host='IP', port=6379, db=0, password='密码', decode_responses=True)
```

---
## 操作

```python
# 删除键
r.delete(键)

# 清空所有数据
r.flushdb()

# 是否 键存在
r.exists(键)

# 重命名
r.rename(原键名, 新键名)
```




