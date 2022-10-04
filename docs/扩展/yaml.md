# yaml

数据序列化语言, 用于 存储, 序列化, 扩展名为.yml .yaml

---
## 纯量

```yaml
name: 啦啦啦  # 字符串
version: 1.2  # 小数
port: 6331  # 整数
stdin: true  # bool
import: null  # 空值
import2: ~  # 空值
date: 2022-04-11  # 日期
time: 2022-04-11T09:30:10+08:00  # 时间
```

## 多行内容

```yaml
# 多行内容 每行都有换行符
data3: |
  多行内容
  多行内容
  多行内容
  
# 多行内容 结尾有换行
data: >
  多行内容
  多行内容
  多行内容

# 多行内容 结尾无换行符
data2: >-
  多行内容
  多行内容
  多行内容
```

## 数组

```yaml
ports:
  - 5532
  - 3345
  - 4452

ports2: [556,844,528]
```

## 对象

```yaml
container:
  name: mysql
  image: mysql
  port: 3306
  version: 5.7
```

## 锚点与引用

```yaml
# 锚点
server: &ip 127.0.0.1

# 引用
server2: *ip
```
