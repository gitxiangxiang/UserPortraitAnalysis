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
from .views import test_view

app_name = "user_profiles"
urlpatterns = [
    path('tests/', test_view.StationListView.as_view()),
    path('test_for_front/', test_view.test_for_front),
    path('', test_view.index, name='index'),
    path('charts/', test_view.charts),
    path('save/', test_view.save_excel),
    path('test/', TestService.TestPersonalAppealDao.test_gdocf2),
    path('test/<str:field_name>/', TestService.TestPersonalAppealDao.test_gdocf)

]



