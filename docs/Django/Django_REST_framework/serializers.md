# serializers



[toc]



---

## 类

序列化名称 名称ModelSerializer    反序列化名称 名称ModelDeserializer    

一般和 models 字段对应

`from rest_framework import serializers`

`from .models import 数据库`



```python
class 名称Serializer(serializers.Serializer):
    字段 = serializers.类型(选择)
```

### 类型
SerializerMethodField  只读 任何类型的数据



```python
class 名称Serializer(serializers.ModelSerializer):
    名称 = 主键()				主键 是其他的 ModelSerializer类 多个数据 many=True
    名称 = 外键()				外键字段添加 related_name='名称' 名称需要一直
    名称 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  在主键显示外键 Model字段需要related_name='名称' 名称需要一直

    # 字段
    class Meta:
        model = 数据库				绑定数据库
        fields = '__all__'			导入所以字段
        fields = ('字段','字段',...)		导入指定字段
        depth = 1  # 往下深入几层
```

### 选择

用来参与反序列化

`required=True`        必填

`max_length=4`          最大

`min_length=4`          最小

`read_only=True`      只返回不提交  

`write_only=True`     只提交不返回

`help_text='内容'`    提示

`required=True`       必填项

`read_only=True`     只参与序列化

`write_only=True`    只参与反序列化



错误提示

`error_messages={    
    'blank': '请输入验证码',
    'max_length': '验证码格式错误',
    '选择': '没有满足的提示内容',
}`    



### 字段

当前登录的用户 覆盖用户字段





---

## 验证

Serializer类里



验证  接收传递的字段

```python
def validate_字段(self, 字段):
    if True:  自行填条件
        raise serializers.ValidationError('内容')  # 抛出异常 
    data = self.initial_data['数据']  # 接收数据  数据名称
    data = 字段['数据']  # 接收数据  数据名称
    print(字段)  # 字段的数据内容
    return 字段  # 正确返回字段
```



验证 全部字段  attrs全部数据

```python
def validate(self, attrs):
    # 代码
    raise serializers.ValidationError('内容')  # 抛出异常 
    return attrs  # 正确返回字段
```



---

## 保存数据库

验证通过后保存到数据库



```python
def create(self, validated_data):

    return 数据库.objects.create(**validated_data)
```
`self.context['request'].user`  获取当前登录的用户


`validated_data['user']`  字段

---

## 自定义字段

字段代表访问的字段方法    字段方法会返回值给前端

```python
class 名称Serializer(serializers.Serializer):
    ....
    # 字段
    名称 = serializers.SerializerMethodField()
    
    def get_字段名称(self, obj):
        return 返回内容
```

obj代表本次序列化的对象

`obj.get_model字段()`    获取本次序列化model字段的值



---

## 字段添加选项



```python
class 名称Serializer(serializers.ModelSerializer):

    class Meta:
        ...
        
        extra_kwargs = {
            '字段': {
                '选择': '值' 
            },
            '字段': {
                '选择': '值'  
            },
        }
```

## 详情



[^1]: 有时需要传递参数 serializers类(data=request.data, context={'request': request})

