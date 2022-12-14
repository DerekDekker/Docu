# open

文件读取


| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |

---

## 文件

```python
# 打开
名称 = open(r'路径',打开方式,encoding="编码")
```

```python
with open(r'路径', 'r', encoding='utf-8') as f:
    # 代码
```

!!! note ""

    编码可以不写默认ANSI

---
## 方法

`变量.read(参数)`         读取文件内容，参数表示读取个数

`变量.readline()`        每次读取一行

`变量.readlines()`       返回一个列表

`变量.write()`              写入

`变量.writelines()`     可以把列表写入

`变量.seek(0)`              光标返回开始位置

`变量.close()`              关闭文件连接

`变量.flush()`              保存，缓冲区的内容写入磁盘