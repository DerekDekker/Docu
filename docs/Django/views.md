# views

进行逻辑处理


---

## 请求处理



方法

```python
def 名称(request):
    # 代码
```



类

```python
from django.views.generic.base import View

class 名称(View):
    def get(self,request):					# get提交
        # 代码
        
    def post(self,request):					# post提交
        # 代码
```



---

## 逻辑

逻辑处理



### 路径

`request.path`    返回路径

`request.get_full_path()`    返回完整路径



### 用户

`request.user`    获取登陆用户对象

`request.user.is_authenticated`    如果登陆返回对象，用于判断是否登陆加上if



### 密码

`from django.contrib.auth.hashers import make_password`

`make_password(pass_word)`    密码加密保存，pass_word是变量，可以用来把密码加密在提交到数据库里



----

## 表单提交

前端表单提交后端进行的处理



### 表单

`request.method == '方式'`    判断提交类型,加上if,	方式：GET POST

`request.方式.get('名称',默认值)`    获取值,	方式：GET POST

`request.FILES.get('图片name')`    获取图片， 需要form 属性  enctype="multipart/form-data"



### Form

`from 目录.forms import 类`    导入表单

`名称 = forms类() `   初始化表单对象



提交

`名称 = forms类(request.POST,request.FILES,instance=request.user)`    初始化表单对象[^1]

`if 表单对象.is_valid():`    判断是否合法

`表单对象.cleaned_data['字段']`    获得传递值



---

## 数据库

进行数据库的操作



名称 = model类()    实例化数据库

数据库.字段 = '值'    赋值

数据库.save()    添加到数据库



---

## 返回页面



### 返回网页

`from django.shortcuts import render`

`return render(request,'table.html',{'字典':字典})`    显示HTML网页



### 返回代码

`from django.http import HttpResponse`

`return HttpResponse("<h1>Hi</1>")`    显示HTML



### 跳转网页

`from django.shortcuts import redirect`

`return redirect('网址')`    跳转网页



### 反向URL

`from django.http import HttpResponseRedirect`

`from django.urls import reverse`

`return HttpResponseRedirect(reverse('URL名称',args=(参数,))) `    反向URL



---

## 详情

[^1]: request.FILES代表获取上传文件,instance代表修改对象之后可以直接save()



