# templates

前端HTML模板文件


---

## 标签



`{{变量}}`    变量

​    `变量.url`    显示models图片

`{{ user.username }}`    用户属性

`{% load staticfiles %}	`    加载标签库

`{% static '' %}`    样式标签

`{% for %}`    循环遍历

​    `{% endfor %}`    如果没有值输出这个

`{% if %}`    判断

​    `{% elif %}`    多层判断

​    `{% else %}`    如果都不复合输出这个

`{% url 'URL名称' 参数 %}`    反向URL

`{% csrf_token %}`    安全验证,写在表单里

`{{ forlop.counter }}`    for计数，加在for里

`{% autoescape off %}`    输出数据库里的HTML

​    `{%end autoescape off %}`    



---

## 过滤器

{{变量|过滤器:"值"}}



`add`    加法,变量加上值

`cut`    从字符串中移除指定的字符

`date`    格式化日期字符串

`default`    如果变量是False空字符串,就替换成默认值

`safe`    开启自动转义

`slice`    切片

`join`    用指定分隔符链接列表



---

## 系统变量

`request.path`    当前路径，可以配合slice

`request.user.is_authenticated`    是否登陆，可以配合if判断是否登陆



----

## 页面

进行页面的拼接



### 模板

`{% include '路径' %}`

`{% include '路径' with 变量1='值' 变量2='值'... %}`    传递变量



### 继承

`{% block 命名 %}内容{% endblock %}`    父模板

`{% extends "父模板" %}`    子模板    继承,写在子模板顶部

`{% block 父模板名 %}重写{% endblock %}`    重写父模板

​    `{{ block.super }}`    父模板原本内容，写在子模板block里



---

## 扩展

## html

`<a href="?sort=hot">链接</a>`    ?后是 名称=参数



### 错误

`{% for key,error in  register_form.errors.items %}{{ key }}:{{ error }}{% endfor %}`    错误提示， register_form是forms对象，key代表字段 error代表内容

`{% if register_form.errors.email %}{% endif %}`    错误显示内容， register_form是forms对象，email是forms对象是否错误字段

`{{ register_form.email.value }}`    返回上次填写的信息，register_form是forms对象，email是forms对象字段





