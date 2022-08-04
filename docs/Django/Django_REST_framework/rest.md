###### rest



[toc]



---

## 请求处理



### APIView

`from rest_framework.views import APIView`

`from rest_framework.response import Response` 



```python
class 名称(APIView):
    def get(self, request):
        # 代码
        return Response('数据', status=状)
```

`request.data`    接收的全部数据    获取body

`request.data['a']`    接收数据    获取body

`request.GET.get('ss', )`    接收数据    获取params

`request.user` 返回用户对象

`request.auth` 返回任何附加的认证上下文

`request.method` 请求类型 GET POST

---

## 序列化

`from .serializers import 类`



`名称 = serializers类(数据库对象)`    序列化    多条数据 many=True

`serializers对象.data`    序列化的内容    用于返回



---

## 反序列化

```python
名称 = serializers类(data=request.data, many=False)
if 名称.is_valid():
    名称.save()
```

`serializers对象.is_valid(raise_exception=True)`    验证失败抛出异常, 并给出提示信息
`many=False`    单增
`many=True`      群增



错误提示

```python
return Response(serializers对象.errors)
```



判断接收数据类型
```python
isinstance(request.data, list)
```



---

## 类
`pip install django-filte`


settings.py
```python
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]
```


```python
from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend    过滤
from .serializers import 类
from .filters import 类



class 名称(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    备注会自动生成 API 文档
    list:
        列表
    delete:
        删除
    '''
    queryset = 数据库.objects.all()
    serializer_class = serializers类				类没有()

    pagination_class = 分页类

    过滤  搜索  排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)    
    
    过滤
    filterset_fields = ('字段', '字段')

    搜索
    search_fields = ('字段', '字段', '外键__字段')
    
    排序
    ordering_fields = ('字段', '-字段')  
    
    默认顺序
    ordering = ['username']

    
    哪个字段作为访问数据 默认是ID
    lookup_field = '字段'
    
    方法可以直接URL访问 detail 是否详情
    @action(detail=False, methods=['get', 'post'], permission_classes=[IsAdminUser])
    def 方法名(self, request):
        # 代码
        return Response(status=status.HTTP_201_CREATED)
    
    分页
    @action(detail=False, methods=['get', 'post'], permission_classes=[IsAdminUser])
    def 方法名(self, request):
        pg = PageNumberPagination类()
        pg_queryset = pg.paginate_queryset(queryset=Model对象, request=request, view=self)
        名称_serializers = ThemeSectionAuditSerializers(pg_queryset, many=True)

        return pg.get_paginated_response(theme_section_audit_serializers.data)
```

需要基础

`viewsets.GenericViewSet`



单个数据 详情

`mixins.RetrieveModelMixin`    增加继承[^1]



获取列表

`mixins.ListModelMixin`    增加继承



添加功能

`mixins.CreateModelMixin`    增加继承



更新功能

`mixins.UpdateModelMixin`    增加继承



删除功能

`mixins.DestroyModelMixin`    增加继承



加删改查 全部功能

`viewsets.ModelViewSet`    只需继承



### 自定义处理

```python
from rest_framework import mixins, viewsets
from .serializers import 类

class 名称(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers类


    # 可选
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```
### 过滤查询集
用户只能查看自己的内容


```python
def get_queryset(self):
    return 数据库.objects.filter(user=self.request.user)
```



去掉属性

`queryset`



### 自定义通用过滤
过滤掉一些内容 如只能查看自己的内容


filters.py
```python
from rest_framework import filters

class Is名称(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 代码
        return queryset.filter(字段=值)
```

类的属性

`filter_backends = (Is名称, )`



---
## 属性
`from rest_framework.renderers`

`renderer_classes = [StaticHTMLRenderer]` 不进行渲染

---

## 配置



### settings

settings里INSTALLED_APP

```python
'rest_framework',
'django_filters',
```



### 分页

全局分页
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
}
```


```python
from rest_framework.pagination import PageNumberPagination

class 名称(PageNumberPagination):
    page_size= 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100
```




### URL

#### 登录
`path('api-auth/', include('rest_framework.urls')),`    

#### API文档

`from rest_framework.documentation import include_docs_urls`

`path('docs/', include_docs_urls(title='文档')), `

settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
```

---
### 映射

```python
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
或
urlpatterns += router.urls
```

---

## 权限

`from rest_framework.permissions import *`



`permission_classes = [权限, 自定义权限]`    类里的属性

+ `AllowAny`    允许
+ `IsAuthenticated`    需要验证
+ `IsAdminUser`  需要管理员
+ `IsAuthenticatedOrReadOnly`  未认证只读



### 自定义权限
permissions.py [^3]

```python
from rest_framework import permissions

class Is名称(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = '没有权限'

    def has_object_permission(self, request, view, obj):
        # 是否只读访问
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
```
返回
   + True 通过
   + False 未通过

方法重写
+ has_permission(self, request, view)  视图级
+ has_object_permission(self, request, view, obj)  实例级[^5]


`permissions.SAFE_METHODS`  只读访问 配合if 属性

`obj.user`    关联的用户[^2]



---

## 认证



settings.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken',
    ...
]

REST_FRAMEWORK = {
    ...permissions
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
    ...
}
```



urls.py

```python
from rest_framework.authtoken import views

urlpatterns = [
    ...
    path('api-token-auth/', views.obtain_auth_token)
    ...
]
```

POST请求URL 用帐号和密码得到密钥

参数
username
password



每次访问 请求头 带上密钥

"Authorization":
"token 密钥"



---

## JWT认证

这种认证更安全 更高效

[文档](https://jpadilla.github.io/django-rest-framework-jwt/ 'JWT认证文档')

`pip install djangorestframework-jwt`     [^4]



settings.py

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ]
    ...
}
```



settings.py    可选配置 

```python
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),    # 过期时间 天 单位
    'JWT_AUTH_HEADER_PREFIX': 'JWT',			   # 请求头 变量设置
}
```



urls.py

```python
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...
    path('api-token-auth/', obtain_jwt_token),
    ...
]
```

POST请求URL 用帐号和密码得到密钥
参数
username
password

每次访问 请求头 带上密钥

"Authorization":
"JWT 密钥"



---

## 扩展


### 状态码

`from rest_framework import status`



`{'数据', status=status.HTTP_200_OK}`    返回数据

`{'message': '成功', status=status.HTTP_200_OK}`   操作提示



---

## 详情



[^1]: 列表页面URL/数据ID    URL/id
[^2]: 改动数据就必须是本用户才可以执行
[^3]: 新建文件

[^4]: 需要安装
[^5]: self.check_object_permissions(request, obj) 非实例级需要在方法里调用



