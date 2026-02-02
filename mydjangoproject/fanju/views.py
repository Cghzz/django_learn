from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
# Create your views here.
def cccgg(request):
    return HttpResponse("张三喜欢李四")

def django(request):
    return HttpResponse("学习django")

def django1(request):
    print(request.GET.get("page"))
    page=request.GET.get("page")
    if page=="1":
        return HttpResponse('1')
    else :
        return HttpResponse('页码错误')
    #return render(request,'django1.html')

def django2(request):

    return HttpResponse("学习django2")
def flask(request):
    return HttpResponse("学习flask")

def fastapi(request):
    return HttpResponse("学习fastapi")

def select_django(request):
    get_django_all = models.Django1.objects.all()
    print(get_django_all)
    return HttpResponse("查")
def delete_django(request):
    id1=models.Django1.objects.get(id=1)
    id1.delete()
    return HttpResponse("删")
def update_django(request):
    id2=models.Django1.objects.get(id=2)
    id2.name='django1'
    id2.time_class='100'
    id2.save()
    return HttpResponse("改")
def insert_django(request):
    models.Django1.objects.create(name='django3',time_class='30')
    return HttpResponse("增")