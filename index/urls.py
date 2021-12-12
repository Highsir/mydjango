from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # path('',views.index),
    path('<year>/<int:mouth>/<slug:day>', views.mydate, name='mydate'),
    # re_path('(?P<year>[0-9]{4})/(?P<mouth>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),
    path('', views.index, name='index'),
    path('trunTo', RedirectView.as_view(url='/'), name='trunTo'),
]


# urlpatterns = [
#     url('^$', views.index),
#     url('^new/$', views.new)
# ]