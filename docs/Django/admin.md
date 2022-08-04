# admin



[toc]

2

---

## 设置



### 命令

`python manage.py createsuperuser`    添加管理员



---

## 基础

`import xadmin`

`from 应用.models import 模型类`



字段

```python
class 名称Admin(admin.ModelAdmin):			
    list_display = ('字段','字段',...)		# 显示字段，也可以是Models里定义的函数
    search_fields = ('字段','字段',...)		# 搜索字段
    list_filter = ('字段','字段',...)		# 过滤条件
    fields = ('字段','字段',...)		# 不显示编辑
    字段__外键					# 关联外键,可以放在如: 搜索
    ordering = ['-字段']			# 排序
    readonly_fields = ['字段','字段',...]	# 只读字段，不可编辑
    exclude = ['字段','字段',...]		# 隐藏字段
    list_editable = ['字段','字段',...]		# 哪些字段可以在列表页直接修改
    refresh_times = [3,5,...]			# 几秒刷新一次，设置完可以在列表页选择
    raw_id_fields = ('外键字段', '外键字段')    # 搜索显示
```

`admin.site.register(模型类,名称Admin)`



---
## 增加自定义按钮
```python
actions = ['button']

def button(self, request, queryset):
    print(self)
    print(request)
    print(queryset)

# 显示的文本，与django admin一致
button.short_description = '测试按钮'
# icon，参考element-ui icon与https://fontawesome.com
button.icon = 'fas fa-audio-description'

# 给按钮追加自定义的颜色
button.style = 'color:black;'

# 给按钮增加确认
button.confirm = '是否确定通过'
```

---
## 配置



### 安装

`pip install django-simpleui`    需要安装



settings.py

```python
INSTALLED_APP = [
    'simpleui',
    '...',
]
```

---

## 扩展

settings.py
```python
SIMPLEUI_INDEX = 'https://www.baidu.com'  # 首页跳转
SIMPLEUI_ANALYSIS = False  # 不收集分析信息

SIMPLEUI_ICON = {
    '关注关系': 'fas fa-users',
}
```

### 相关

文档

https://simpleui.88cto.com/docs/simpleui/


图标

https://fontawesome.com/icons


