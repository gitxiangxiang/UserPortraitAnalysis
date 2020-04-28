"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import test_view, persistent_appeal_view, personal_appeal_view

app_name = "user_profiles"
urlpatterns = [
    # 各级分类
    path('label_gjflH/', personal_appeal_view.each_classification),
    # 工单信息
    path('order_info/', personal_appeal_view.order_info),
    # 时间规律
    path('time_trend/', personal_appeal_view.time_appeal),
    # 主页
    path('', test_view.index, name='index'),
    # 词云图
    path('word_cloud/', personal_appeal_view.word_cloud),
    # 存储Excel
    path('persistent_excel/', persistent_appeal_view.do_persistent),
    # 上传Excel
    path('upload_excel/', persistent_appeal_view.upload_excel),
    # 测试
    path('test/', test_view.test_for_front)

]



