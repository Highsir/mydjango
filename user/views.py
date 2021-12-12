from django.http import HttpResponse


def index(request):
    return HttpResponse('this is userindex')


def userLogin(request):
    return HttpResponse('this is userLogin')