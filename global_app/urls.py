from global_app.views import index
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from global_app.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('addtenant/', create_tenant_page, name='addtenant'),
    path('addusers/', create_users_page, name='addusers'),
]