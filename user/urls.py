from django.urls import path
from . import views
from .views import registerView, setpsView, logoutView, findpsView

urlpatterns = [
    # path('index.html', views.index, name='index'),
    path('login.html', views.userLogin, name='userLogin'),
    path('register.html', registerView, name='register'),
    path('setps', setpsView, name='setps'),
    path('logout', logoutView, name='logout'),
    path('findps', findpsView, name='findps'),
]