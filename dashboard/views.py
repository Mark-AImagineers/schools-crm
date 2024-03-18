from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard_view(request):
    #this is where the dashboard logic goes
    return render(request, 'dashboard/dashboard.html')