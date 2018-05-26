from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ProtectedError
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from hrs.models import Dept,Emp


def index(request):
    ctx = {
        'greeting':'你好'
    }
    return render(request,'index.html',ctx)

def depts(request):
    ctx = {
        'dept_list':Dept.objects.all()
    }
    return render(request,'dept.html',context=ctx)

def emps(request,no='0'):

    # print(request.METE.['HTTP_']
    no = request.GET['no']
    # dept = Dept.objects.get(pk=no)使用了惰性查询，如果不是非得取到数据那么不会发出SQL语句
    # 这样做是为了节省服务器内存的开销 - 延迟加载 - 节省空间的势必浪费时间

    # QuerySet
    Emps = Emp.objects.filter(dept__no=no)
    if Emps.count()>0:
        ctx = {
            'emp_list':Emps
        }
        return render(request,'emp.html',context=ctx)
    else:
        return HttpResponse('<h1>没有此员工</h1>')

def deldept(request):
    try:
        no = request.GET['no']
        dept = Dept.objects.get(pk=no)
        dept.delete()
    # ctx = {
    #     'ctx':Dept.objects.all()
    # }
    # return render(request,'dept.html',context=ctx)
    except (ProtectedError,ObjectDoesNotExist):
        return HttpResponse('<h1>不是一个空部门</h1>')
    return redirect(reversed('/hrs/depts'))

# def deldept(request):
class Add_data(forms.Form):
    no = forms.IntegerField(label='部门编号')
    name = forms.CharField(max_length=20,label='部门名称')
    location = forms.CharField(max_length=10,label='部门地址')
    excellent = forms.BooleanField(label='是否优秀')


def add1(request):
    if request.method == 'GET':
        f = Add_data()
    else:
        f = Add_data(request.POST)
        if f.is_valid():
            Dept(**f.cleaned_data).save()
            f = Add_data()
    return render(request,'add1.html',{'f':f})
