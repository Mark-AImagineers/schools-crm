from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('dash/', dashboard_view, name='dashboard'),
]