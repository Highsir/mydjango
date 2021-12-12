from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    # value = 'This is test.'
    # print(value)
    # return render(request, 'index.html')
    # print(reverse('index:trunTo'))
    # return redirect(reverse('index:mydate', args=[2021,12,12]))
    # html = '<h1>Hello World</h1>'
    # return HttpResponse(html, status=200)
    if request.GET.get('error', ''):
        raise Http404("Page is not exits")
    else:
        value = {'title': 'Hello MyDjango'}
        content = {'key': 'This is MyDjaogo'}
        # return render(request, 'index.html', context=value)
        return render(request, 'index.html', locals())


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