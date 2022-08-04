# model



[toc]



---

## 命令



`python manage.py makemigrations 应用名`

`python manage.py migrate 应用名`



---

## 模型

`from django.db import models`    导报



```python
class 表名(models.Model):
    字段名 = models.类型Field(选项)
```

### 选项

`verbose_name='名称'`                          说明

`min_length = 5`                                  最小长度

`max_length=20`                                   最大长度

`nul=False`                                 是否可以为空    

`blank=True|False`

`default='值'`                                    默认值

`primary_key=True|False`                  设置主键，类型Auto

`unique=False`                                   唯一索引

`db_index=False`                                普通索引

`choices=(('',''),('',''),...)	`     单选

`upload_to='路径'`                            上传路径

#### 外键需要添加

`on_delete=models.CASCADE`             级联

`on_delete=models.DO_NOTHING`        不级联



### 类型

`Auto`                                               整型，自增长，用于主键

`Char`                                               字符串

`Boolean`                                          布尔

`Date`                                               日期

`DateTime`                                        日期时间

`Decimal`                                          精确小数

`Float`                                             浮点小数

`Integer`                                          整型

`Text`                                               文本内容，无限长度

`Image`                                             图片

`File`                                               文件



### 外键

`OneToOne`                                       一对一

`ForeignKey(没有Field)`                一对多

`ManyTomany`                                  多对多



---

## 方法

放在模型类里的方法



### 设置

```python
class Meta:
    verbose_name = '名称'
    verbose_name_plural = verbose_name	  # 显示的名称
    db_table='名称'		          # 数据表名
    proxy = True		          # 不进行注册(不生成表),还会保留Models功能
    unique_together = ('字段', '字段')	  # 联合唯一索引
```



### 显示数据

```python
def __str__(self):
    return self.字段			          # 显示数据
```



### 方法

像字段一样调用

```python
@property
def 名称(self):
    from 应用.models import 类            # 可以导入类
    return self.某表_set.all().count()    # 可以有return，self代表本表，可以在HTML调用

名称.short_description = '国家'  # 在admin显示字段名
```



---

## 扩展



### 数据增加的时间

```python
add_time = models.DateTimeField('发帖时间',auto_now_add=True)
last_edit = models.DateTimeField('修改时间',auto_now=True)
```





