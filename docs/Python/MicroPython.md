# 基础

[文档](http://docs.micropython.org/en/latest/index.html)

```python
import machine
```

---
## 电平输出

```python

pin12 = machine.Pin(2, machine.Pin.OUT)  # GPIO

# 高电平
pin12.value(1)

# 低电平
pin12.value(0)

```

---
## PWM

PWM（Pulse Width Modulation）简称脉宽调制

```python
from machine import Pin, PWM

led2 = PWM(Pin(2))  # GPIO
led2.duty(100)  # 最大 1024
```

### 呼吸灯

```python
from machine import Pin, PWM
import time

led2 = PWM(Pin(2))
led2.freq(1000)
while True:
    for i in range(0, 1024):
        led2.duty(i)
        time.sleep(0.001)
```

---
## 网络

```python
import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # 激活

# Wi-Fi 连接
wlan.connect('名称', '密码')

```


```python
# 搜索 Wi-Fi
wlan.scan()  

# 是否 已连接 AP 返回 True | False
wlan.isconnected()      

# 获取MAC地址
wlan.config('mac')

# 获取IP 返回的第一个是局域网IP
wlan.ifconfig()
```

### AP模式

开启热点

```python
import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='网络名')
# 最大连接数 可选
ap.config(max_clients=10)
```

```python
# 创建带有密码的热点
ap.config(essid='网络名', password='密码', authmode=3)
```

!!! none ""

    authmode 为模式

    0 – 开放

    1 – WEP

    2 – WPA -PSK

    3 – WPA 2-PSK

    4 – WPA / WPA2-PSK
