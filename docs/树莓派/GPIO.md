# GPIO

---
## 介绍

| 关键字            | 描述        |
|----------------|-----------|
| /dev/ttyS0     | 串口        |
| /dev/ttyUSB0   | USB转窜口    |

---
## 命令

```shell
# 参看全部接口
ls -l /dev/tty*

```

---

## 获取串口数据

```shell
minicom -b 9600 -o -D /dev/ttyUSB0
```
