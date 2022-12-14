# request

网络请求

导包

import requests

---
## 请求 

```python
x = requests.post('url')

x = requests.request(method='请求方式', url='url', **kwargs)

```
??? note "参数"

    kwargs  13个访问参数

    params = 字典或列表        传递参数 可用于GET请求

    data = 字典或列表或文件     传递数据

    json = 字典               传递json

    headers = 字典            修改协议头

    cookies =

    files = {'变量': open('文件', 'rb')}  传递文件

    timeout = 10              超时时间 秒 抛出异常

    proxies =                 设置代理服务器

    allow_redirects = True    允许重定向

    stream = True             获取内容立即下载

!!! tip "请求方式"

    get 主要方法   

    post 新增请求    

    put 覆盖请求   

    patch 修改请求 

    delete 删除请求

---

## 属性

```python
# 打印网页内容
x.text

# 状态码
x.status_code

# 头部信息 服务器 返回
x.headers

# 头部信息 客户端 发送
x.request.headers

# 猜测网页的编码形式
x.encoding

# 分析网页的编码形式
x.apparent_encoding

# 二进制形式 图片等
x.content

# json转字典
x.json()
```

---

# 方法

```python
# 更改编码
x.encoding = 'utf-8'
```

---

## GraphQL

GraphQL 方式请求

```python
# QUERY 值
query = """值"""

# GRAPHQL VARIABLES 值
variables = {'名称': '值'}

request = requests.post(url, json={'query': query, 'variables': variables})
```

