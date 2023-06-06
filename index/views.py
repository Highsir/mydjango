import os

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import StreamingHttpResponse
from django.http import FileResponse, response
from django.views.generic import RedirectView, TemplateView, ListView, DetailView
# from .form import PersonInfoForm
from django.views.generic.edit import FormView

# from index.models import PersonInfo
# from index.form import VocationForm
from index.form import VocationForm


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
    # if request.method == 'GET':
    #     # 类方法的使用
    #     print(request.is_secure())
    #     print(request.is_ajax())
    #     print(request.get_host())
    #     print(request.get_full_path())
    #     print(request.get_raw_uri())
    #     # 属性的使用
    #     print(request.COOKIES)
    #     print(request.content_type)
    #     print(request.content_params)
    #     print(request.scheme)
    #     # 获取GET的请求参数
    #     print(request.GET.get('user', ''))
    #     return render(request, 'index.html')
    # elif request.method == 'POST':
    #     print(request.POST.get('user', ''))
    #     return render(request, 'index.html')

    # 验证自定义标签
    # return render(request, 'index_template.html', locals())
    # 验证自定义过滤器
    # value = "Hello Python"
    # return render(request, 'index_filter.html', locals())

    # 验证jinja2
    # value = {'name': 'This is jinja2'}
    # return render(request, 'index_jinja2_template.html', locals())

    # jinja自定义过滤器
    value = {'name': 'This is jinja2'}
    return render(request, 'index_replace.html', locals())

def result(request):
    return HttpResponse('Success')


def create(request):
    r = redirect(reverse('index:index'))
    r.set_signed_cookie('uuid','id',salt='myDjango', max_age=10)
    return r

def myCookie(request):
    cookieExist = request.COOKIES.get('uuid', '')
    if cookieExist:
        try:
            request.get_signed_cookie('uuid', salt='myDjango')
        except:
            raise Http404('当前Cookie无效')
        return HttpResponse('cookie: '+ cookieExist)
    else:
        raise Http404('当前访问没有Cookie')

def getHeader(request):
    """请求头实现反爬虫"""
    header = request.META.get('HTTP_SIGN', '')
    if header:
        value = {'header': header}
    else:
        value = {'header': 'null'}
    return JsonResponse(value)

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


class trunTo(RedirectView):
    permanent = False
    url = None
    pattern_name = 'index:index'
    query_string = True

    # 重写get_redirect_url
    def get_redirect_url(self, *args, **kwargs):
        print('This is get_redirct_url')
        return super().get_redirect_url(*args, **kwargs)

    # 重写get
    def get(self, request, *args, **kwargs):
        print(request.META.get('HTTP_USER_AGENT'))
        return super().get(request, *args, **kwargs)


class clsIndex(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title': 'This is GET'}

    # 重写get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'I am myDjango'
        return context

    def post(self, request, *args, **kwargs):
        self.extra_context = {'title': 'This is POST'}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


# class indexList(ListView):
#     template_name = 'view.html'
#     extra_context = {'title': '人员信息表'}
#     queryset = PersonInfo.objects.filter().all()
#     paginate_by = 1
#
# class indexDetail(DetailView):
#     template_name = 'detail.html'
#     extra_context = {'title': '人员信息表'}
#     # 设置模型的查询字段
#     slug_field = 'age'
#     # 设置路由的变量名，与属性slug_field实现模型的查询操作
#     pk_url_kwarg = 'pk'
#     model = PersonInfo
#     # queryset = PersonInfo.objects.all()
#
# class indexFormView(FormView):
#     initial = {'name': 'Betty', 'age': 20}
#     template_name = 'index_form_view.html'
#     success_url = '/result'
#     form_class = PersonInfoForm
#     extra_context = {'title': '人员信息表'}

def index_form(request):
    if request.method == "GET":
        v = VocationForm()
        return render(request, 'index_form.html', locals())
    else:
        v = VocationForm(request.POST)
        if v.is_valid():
            title = v['title']
            c_title = v.cleaned_data['title']
            print(c_title)
            return HttpResponse('提交成功')
        else:
            error_msg = v.errors.as_json()
            print(error_msg)
            return render(request, 'index_form.html', locals())