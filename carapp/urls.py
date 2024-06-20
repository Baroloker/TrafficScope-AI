# carapp/urls.py

from django.urls import path
from .views import upload_image, index, dashboard, login_view, trace_car, home

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),  # 定义一个上传图片的路径
    path('', index, name='index'),  # 路由到 index 页面
    path('dashboard/', dashboard, name='dashboard'),  # 路由到 dashboard 页面
    path('login/', login_view, name='login'),
    path('trace/', trace_car, name='trace_car'),
    path('home/', home, name='home')
]
