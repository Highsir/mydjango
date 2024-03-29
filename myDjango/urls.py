"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from index.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(('index.urls', 'index'), namespace='index')),
    # path('', include(('user.urls', 'user'), namespace='user')),
    path('admin/', admin.site.urls),
    path('', include(('user.urls', 'user'), namespace='user')),
]
# 全局404
handler404 = 'index.views.pag_not_found'

# 全局500
handler500 = 'index.views.page_error'

# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url('^', include('index.urls'))
# ]