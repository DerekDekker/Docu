# ORM

---
## 查询



表.objects.all()				查询所以值，可以for遍历


表.objects.get(条件)				查询，只能返回一个值

表.objects.filter(条件)				返回匹配的值

表.objects.exclude(条件)			返回不匹配的值

```python title="方法"
.values('字段','字段'...)			查询字段,返回字典

.values_list('字段','字段'...)			查询字段,返回元组

.count()					多少条记录

.exists()					是否有数据

.order_by('-字段')[:3]    加-代表从大到小，后面可以加切片，获得数据
```


### 关系


外键对象.外键字段				显示外键的所有主键

主键对象.外键表_set				显示主键的所有外键

外键字段__主建字段				在外键显示主键字段

外键表__外键字段				在主键显示外键字段


### 时间

.filter(时间字段__gte='2021-03-17 20:11:58')  大于等于这个时间  开始时间  gt大于

.filter(时间字段__lte='2021-03-17 20:11:58')  小于等于这个时间  结束时间  lt小于


### Q

```python

from  django.db.models import Q

...(Q(字段=变量)|Q(字段=变量)|Q(字段=变量)...)		或者，搜索条件

```

### 模糊搜索

```python
...(字段__icontains=变量)				模糊搜索，icontains前面加i表示忽略大小写
```

### 合并结果

```python
from itertools import chain
querysets = chain(model1, model1)
```

---
## 删除

表.objects.filter(条件).delete()

对象.delete()

---
## 修改
```python
变量 =表.objects.get(条件)
变量.字段  = '内容'
...
变量.save()
```

```python
表.objects.filter(条件).update(字段='内容',...)
```

---
## 增加

```python
表(字段='内容',...).save()
```

```python
表.objects.create(字段='值')
```

```python
变量 = 表()
变量.字段 = '值'
...
变量.save()
```


### 外键

```python
表.objects.create(字段=外键ID)
```

```python
表.objects.create(字段=获取的对象变量）
```

### 表关系

外键对象.外键字段.add(主键对象)

主键对象.外键表_set.add(外键对象)

### 取消表关系

主键对象.外键表_set.remove(外键对象)				删除单个关系

主键对象.外键表_set.clear()					删除全部关系

外键对象.外键字段.remove(主键对象)				删除单个关系

外键对象.外键字段.clear()					删除全部关系

---
### SQL

```python
from django.db import connection
cursor = connection.cursor()		获得游标

cursor.execute('SQL')

cursor.fetchone()			获得单个值
cursor.fetchall()			获得多个值
```