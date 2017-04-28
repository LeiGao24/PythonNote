#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse(u"欢迎光临！！")


def index2(request):
	return render(request,"index.html")


def show(request):
	str = "this is a page"

	return render(request,"show.html",{'string':str})

def showdic(request):
	dic = {'乔峰':'降龙十八掌','段誉':'北冥神功','虚竹':'天山六阳掌'}
	return render(request,"show.html",{'dic':dic})