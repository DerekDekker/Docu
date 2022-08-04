# urls



[toc]



---

## 基础

`from django.urls import path`        url基础导包

`path(正则表达式,view函数,参数,别名,前缀)`    



---

## 访问处理

访问进行处理



### 访问

`from . views import 类`    导入views文件

```python
urlpatterns = [
    path('',类,name='名称'),                   # 访问函数
    path('',类.as_view(),name='名称'),         # 访问类
]
```



### 映射

`from django.conf.urls import include`

```python
urlpatterns = [
    path('app/',include(('应用.urls','名称'))),			# 映射到其他urls进行处理
]
```



---

## 正则表达式

`<表达式:变量>`    在views函数里接收

str    匹配字符串

int    匹配数字

path    匹配任何字符



---

## URL提交

`request.GET.get('参数')`    接收参数值

`/?参数=值`    输入在地址的后面的参数