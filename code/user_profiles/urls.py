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
from .service import TestService
from . import views

app_name = "user_profiles"
urlpatterns = [
    path('tests/', views.StationListView.as_view()),
    path('', views.index, name='index'),
    path('charts/', views.charts),
    path('hello/', views.crud_mongo_test),
    path('test/', TestService.TestPersonalAppealDao.test_gdocf2),
    path('test/<str:field_name>/', TestService.TestPersonalAppealDao.test_gdocf)

]



