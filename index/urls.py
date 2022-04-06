from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views
from .views import *

urlpatterns = [
    # path('',views.index),
    # path('<year>/<int:mouth>/<slug:day>', views.mydate, name='mydate'),
    # re_path('(?P<year>[0-9]{4})/(?P<mouth>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),
    # path('', views.index, name='index'),
    # path('', views.clsIndex.as_view(), name='index'),
    # path('', views.indexList.as_view(), name='index'),
    # path('<pk>/<age>.html', views.indexDetail.as_view(), name='index'),
    # path('', views.indexFormView.as_view(), name='index'),
    # path('result', result, name='result'),
    # path('trunTo', RedirectView.as_view(url='/'), name='trunTo'),
    # path('trunTo', views.trunTo.as_view(), name='trunTo'),
    # path('download/file1', views.download1, name='download1'),
    # path('download/file2', views.download2, name='download2'),
    # path('download/file3', views.download3, name='download3'),
    # path('upload', views.upload, name='upload'),
    # path('uploadPicture', views.uploadPicture, name='picture'),
    # path('create', views.create, name='create'),
    # path('myCookie', views.myCookie, name='myCookie'),
    # path('getHeader', views.getHeader, name='getHeader'),
    # path('', index_form, name='index_form'),
    path('', index, name='index'),
]


# urlpatterns = [
#     url('^$', views.index),
#     url('^new/$', views.new)
# ]