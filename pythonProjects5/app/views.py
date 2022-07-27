# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from app import models


def index(request):
    return render(request, 'login.html')


def register(request):

    error_name = ''
    if request.method == 'POST':

        # 获取用户名 密码
        name = request.POST.get('请输入用户名')
        password = request.POST.get('请输入密码')
        user = request.POST.get('请输入用户身份')
        # 打印 查看参数是否正确
        print("name:"+name)
        print("password:"+password)

        user_list = models.User.objects.filter(name = name).first()
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % name
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'login.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(name = name, password = password, user=user)
            user.save()

            return HttpResponse('<h1>注册成功!</h1>')



