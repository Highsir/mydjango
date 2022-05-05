from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('this is userindex')


def userLogin(request):
    title = '登录'
    pageTitle = '用户登录'
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        if User.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
            return HttpResponse("登录成功")
        else:
            tips = "账号密码错误,请重新登录"
    else:
        tips = '用户不存在, 请重新输入'
    return render(request, 'user.html', locals())


def registerView(request):
    title = '注册'
    pageTitle = '用户注册'
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        if User.objects.filter(username=u):
            tips = '用户已存在'
        else:
            d = dict(username=u, password=p, is_staff=1, is_superuser=1)
            user = User.objects.create_user(**d)
            user.save()
            tips = '注册成功'
    return render(request, 'user.html', locals())


def setpsView(request):
    title = '修改密码'
    pageTitle = '修改密码'
    password2 = True
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        p2 = request.POST.get('password2', '')
        if User.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                user.set_password(p2)
                user.save()
                tips = '密码修改成功'
            else:
                tips = "原始密码不正确"
        else:
            tips = "用户不存在"
    return render(request, 'user.html', locals())


def aewtpaView2(request):
    """
    使用make_password实现密码修改
    :param request:
    :return:
    """
    # 验证
    # from django.contrib.auth.hashers import make_password
    #
    # >> > from django.contrib.auth.hashers import check_password
    # >> > ps = '123456'
    # >> > dj_ps = make_password(ps, None, 'pbkdf2_sha256')
    # >> > ps_bool = check_password(ps, dj_ps)
    # >> > ps_bool

    title = '修改密码'
    pageTitle = '修改密码'
    password2 = True
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        p2 = request.POST.get('password2', '')
        if User.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                dj_ps = make_password(p2, None, 'pbkdf2_sha256')
                user.password = dj_ps
                user.save()
            else:
                print("原始密码不正确")
        else:
            print('用户%s不存在' % u)
    return render(request, 'user.html', locals())


def logoutView(request):
    logout(request)
    return HttpResponse('注销成功')