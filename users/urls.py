from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^say/', views.say, name='say'),
    url(r'^$',views.header, name='header')
]