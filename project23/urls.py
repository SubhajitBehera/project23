"""project23 URL Configuration

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
from django.contrib import admin
from django.urls import path
from app23 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.showIndex,name="main"),
    path('add_emp/',views.add_emp,name="add_emp"),
    path('save_emp/',views.save_emp,name="save_emp"),

    path('view_emp/',views.view_emp,name="view_emp"),
    path('add_acc/',views.add_acc,name="add_acc"),

    path('save_account/',views.save_account,name="save_account"),
    path('view_acc/',views.view_acc,name="view_acc")
]
