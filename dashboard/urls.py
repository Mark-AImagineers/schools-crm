from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
]