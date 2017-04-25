<!-- MarkdownTOC -->

- [Django环境搭建](#django环境搭建)
- [Django基本命令](#django基本命令)
- [Django视图与网址](#django视图与网址)
- [Django模板 templates](#django模板-templates)
- [Django 模板的标签](#django-模板的标签)
- [Django CRUD操作](#django-crud操作)

<!-- /MarkdownTOC -->

###Django环境搭建
- 安装python
- 安装Django  
    + pip install Django.zip
    
###Django基本命令
- 新建一个Django project
    + > django-admin startproject mysite
- 新建app
    + > python manage.py startapp learn
- 启动开发服务器
    + > python manage.py runserver

###Django视图与网址
- 将app加入settings.py
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learn',
]
```

- 创建视图 learn views
``` python
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"欢迎光临")
```

- 设置url视图
``` python
from learn import views as learn_views

urlpaterns = [
    url(r'^$',learn_views.index),
]
```

###Django模板 templates
- 建立模板 learn/templates
``` html
<!DOCTYPE html>
<html>
<head>
    <title>Django 第一个html模板</title>
</head>
<body>
    <h1>LeiGao，欢迎光临！</h1>
</body>
</html>
```
- 处理模板
``` python
from django.shortcuts import render

def index2(request):
    return render(request,'index.html')
```
- 视图设置
``` python
from learn import views as learn_views

urlpatterns = [
    url(r'^$',learn_views.index2)
]
```

###Django 模板的标签

###Django CRUD操作