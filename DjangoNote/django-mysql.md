##Django - mysql 笔记

- 设置数据库引擎
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee',
        'USER':'root',
        'PASSWORD':'12345',
        # 'HOST':''
        # 'PORT':''
    }
}
```
- 安装mysql驱动——mysqlclient

```pip install mysqlclient```

- 创建model类，映射数据库表
``` python
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=4)
    addr = models.CharField(max_length=100)
```
- 同步数据库表
``` 
python manage.py migrate   # 创建表结构

python manage.py makemigrations employee  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate employee   # 创建表结构
```

- 数据库的基本操作：

``` python
from django.shortcuts import render
from employee.models import Employee
# Create your views here.
def mysqldb(request):
    #添加操作
    employee = Employee(name = '乔峰',sex='男',addr='契丹',age=30)
    employee.save()

    #删除操作
    #第一种方式
    employee1 = Employee.objects.get(id=1)
    employee1.delete()
    # 第二种方式
    Employee.objects.filter(id=2).delete()

    #第三种方式
    Employee.objects.all().delete()
    
    #更新操作
    #第一种方式
    employee2 = Employee.objects.get(id = 2)
    employee2.name="段誉"
    employee2.save()
    #第二种方式
    Employee.objects.filter(id = 3).update(name = '虚竹')

    #修改所有的列
    Employee.objects.all().update(name = '乔峰')
    

    #获取操作
    #
    employees = Employee.objects.all()
    for employee in employees:
        print('{0},{1},{2},{3}'.format(employee.name,employee.sex,employee.age,employee.addr))

    #单个取出QuerySet
    emfilter = Employee.objects.filter(id = 7)
    for em in emfilter:
        print(em.name)
    #单个取出object
    emget = Employee.objects.get(id = 9)
    print(emget.name)
    return render(request,'index.html')
```

##表单提交

``` python
def check(request):
    # GET方法提交表单
    # user = request.GET['username']
    # pwd = request.GET['pwd']
    # 
    # POST方法提交表单
    user = request.POST['username']
    pwd = request.POST['pwd']
    
    return HttpResponse('user = {0},pwd = {1}'.format(user,pwd))
```

index.html-post方法提交
注意： {% csrf_token %}

``` html
<form action="/check" method="post">
    {% csrf_token %}
    user: <input type="text" name="username"><br>
    pswd: <input type="password" name="pwd"><br>
    <input type="submit" name="" value="提交"><br>
</form>
```

index.html-get方法提交

``` html
<form action="/check" method="get">
    user: <input type="text" name="username"><br>
    pswd: <input type="password" name="pwd"><br>
    <input type="submit" name="" value="提交"><br>
</form>
```