from django.conf.urls import url

from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^say/', views.say, name='say'),
    # url(r'^$', views.header, name='header'),
    url(r'^demo/', views.demo_view, name='demo'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r"books", views.BookInfoViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所有路由信息追加到django的路由列表中