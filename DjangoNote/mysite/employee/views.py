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