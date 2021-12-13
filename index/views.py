import os

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import StreamingHttpResponse
from django.http import FileResponse


def index(request):
    # value = 'This is test.'
    # print(value)
    # return render(request, 'index.html')
    # print(reverse('index:trunTo'))
    # return redirect(reverse('index:mydate', args=[2021,12,12]))
    # html = '<h1>Hello World</h1>'
    # return HttpResponse(html, status=200)
    # if request.GET.get('error', ''):
    #     raise Http404("Page is not exits")
    # else:
    #     value = {'title': 'Hello MyDjango'}
    #     content = {'key': 'This is MyDjaogo'}
        # return render(request, 'index.html', context=value)
        # return render(request, 'index.html', locals())
    if request.method == 'GET':
        # 类方法的使用
        print(request.is_secure())
        print(request.is_ajax())
        print(request.get_host())
        print(request.get_full_path())
        print(request.get_raw_uri())
        # 属性的使用
        print(request.COOKIES)
        print(request.content_type)
        print(request.content_params)
        print(request.scheme)
        # 获取GET的请求参数
        print(request.GET.get('user', ''))
        return render(request, 'index.html')
    elif request.method == 'POST':
        print(request.POST.get('user', ''))
        return render(request, 'index.html')

def upload(request):
    # 请求方法为POST时， 执行文件上传
    if request.method == 'POST':
        myFile = request.FILES.get('myfile', None)
        if not myFile:
            return HttpResponse('no file for upload')
        f = open(os.path.join('uploadfile', myFile.name), 'wb+')
        for  chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('upload over!')
    else:
        return render(request, 'upload.html')

def uploadPicture(request):
    if request.method == 'POST':
        myFile = request.FILES.get('picture', None)
        if not myFile:
            return HttpResponse('no file for upload')
        f = open(os.path.join('media', myFile.name), 'wb+')
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('upload over!')
    else:
        return render(request, 'picture.html')

def new(request):
    return HttpResponse('This is new page.')


def myvariable(request, year, mouth, day):
    return HttpResponse(str(year) + '/' + str(mouth) + '/' + str(day))


def mydate(request, year, mouth, day):
    return HttpResponse(str(year) + '/' + str(mouth) + '/' + str(day))
    # return HttpResponse(str(year))

def pag_not_found(request, exception):
    """全局404的配置函数"""
    return render(request, '404.html', status=404)

def page_error(requeset):
    """全局500配置函数"""
    return render(requeset, '500.html', status=500)

def download1(request):
    file_path = 'static/1.png'
    try:
        r = HttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=a.png'
        return r
    except Exception:
        raise Http404('Download error')

def download2(request):
    file_path = 'static/2.jpeg'
    try:
        r = StreamingHttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=b.png'
        return r
    except Exception:
        raise Http404('Download error')

def download3(request):
    file_path = 'static/aa.png'
    try:
        f = open(file_path, 'rb')
        r = FileResponse(f, as_attachment=True, filename='c.png')
        return r
    except Exception:
        raise Http404('Download error')