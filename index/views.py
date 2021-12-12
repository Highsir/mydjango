from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    # value = 'This is test.'
    # print(value)
    # return render(request, 'index.html')
    # print(reverse('index:trunTo'))
    # return redirect(reverse('index:mydate', args=[2021,12,12]))
    html = '<h1>Hello World</h1>'
    return HttpResponse(html, status=200)


def new(request):
    return HttpResponse('This is new page.')


def myvariable(request, year, mouth, day):
    return HttpResponse(str(year) + '/' + str(mouth) + '/' + str(day))


def mydate(request, year, mouth, day):
    return HttpResponse(str(year) + '/' + str(mouth) + '/' + str(day))
    # return HttpResponse(str(year))