from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login

from .models import *
from .forms import *

# Create your views here.
def create_tenant_page(request):
    if request.method == "POST":
        tenant_name = request.POST.get('tenant_name')
        #the paid_until value hardcoded to 365 days for now. Later we can change this to a user-defined value (subscriptions)
        paid_until = timezone.now() + timezone.timedelta(days=365)
        on_trial = request.POST.get('on_trial')
        schema_name = request.POST.get('schema_name')
        created_on = timezone.now()

        tenant = Client(name=tenant_name,
                        paid_until=paid_until,
                        on_trial=on_trial,
                        created_on=created_on,
                        schema_name=schema_name,
                        )
        tenant.save()

        domain = Domain()
        domain.domain = f'{schema_name}.schoolscrm.aimagineers.io'
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

        return HttpResponse("Client registered successfully!")
    else:
        return render(request, 'global_app/add_tenant.html')

def create_users_page(request):
    form = CreateUserFormWithTenant()

    if request.method == "POST":
        form = CreateUserFormWithTenant(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'global_app/add_users.html', context)

def index(request): ##the index page is the user login page
    return redirect('')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use the renamed auth_login here
            return redirect('dashboard')
        else:
            # It's better to use messages framework for user feedback
            return HttpResponse("Invalid username or password.")
    
    return render(request, 'global_app/signin.html')