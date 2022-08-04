# beautifulsoup4

用于 HTML解析

导入包

from bs4 import BeautifulSoup

---
## 解析

```python
x = BeautifulSoup('HTML', 'html.parser')  # 解析器 返回标签

x.prettify()             # 输出 美化 去掉/n

# 查找标签名为p，class属性为"title"
x.find_all('p', 'title')

# 寻找符合标签 返回一个结果
x.find("标签",attrs={"属性": "值"})

# 寻找符合标签 返回全部
x.findAll("标签",attrs={"属性": "值"})
```


---
## 属性
返回的标签

`.text`  获取值

`['属性']`  获属性取值