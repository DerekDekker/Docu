settings



---

## 配置



### 数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库',
        'USER': '用户',
        'PASSWORD': '密码',
        'HOST': 'IP',
        'PORT': '端口',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```



### templates

TEMPLATES里

```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
'APP_DIRS': False,
```



### 样式css

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```



### 应用apps

```python
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
```



### 第三方插件extra_apps

```python
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))
```



### 用户文件文件

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



### AbstractUser继承

```python
AUTH_USER_MODEL = 'APP名称.类名'
```



---

## 设置



### 全局

`ALLOWED_HOSTS = ['*']`    外网访问，允许连接的IP，*代表全部 或 域名

`DEBUG = Ture`    开发或生产环境，Ture开发环境，False生产环境



### admin

`LANGUAGE_CODE = ''`    英文en-us 中文zh-hans

`TIME_ZONE = ''`    时区，Asia/Shanghai上海

`USE_TZ = True`    设置是国际时间，True国际时间 False代表本地时间



### cookie

`SESSION_EXPIRE_AT_BROWSER_CLOSE = True`    浏览器关闭时登录失效











