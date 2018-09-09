from django.shortcuts import render
# 导入http响应模块
from django.http import HttpResponse
# 导入数据模型模块
from . import models


def index(request):
    # return HttpResponse("Hello Django")
    students = models.Student.objects.all()

    context = {
        'title': 'Welcome Django learning',
        'status_code': 200,
        'github': 'https://github.com/jm199504',
        'students':students
    }
    return render(request,'index.html',context)
