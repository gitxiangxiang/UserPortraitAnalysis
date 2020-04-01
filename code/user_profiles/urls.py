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
from .views import view

app_name = "user_profiles"
urlpatterns = [
    path('tests/', view.StationListView.as_view()),
    path('', view.index, name='index'),
    path('charts/', view.charts),
    path('save/', view.save_excel),
    path('test/', TestService.TestPersonalAppealDao.test_gdocf2),
    path('test/<str:field_name>/', TestService.TestPersonalAppealDao.test_gdocf)

]



