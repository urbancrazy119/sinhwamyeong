"""sinhwamyeong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from sales import views as sales_view
from report import views as report_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sales/input/', sales_view.insert_data, name='insert_data'),
    url(r'^sales/delete/', sales_view.delete_data, name='delete_data'),

    url(r'^sales/error/', sales_view.error, name='insert_error'),

    url(r'^accounts/login/',login, name='login', kwargs={'template_name':'login.html'}),
    url(r'^accounts/logout/',logout, name='logout'),
    url(r'^report/daily/',report_view.daily_report, name='daily'),
]

