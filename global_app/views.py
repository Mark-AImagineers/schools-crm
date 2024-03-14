from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from .models import *

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
    if request.method == "POST":
        email = request.POST.get('email')

        # Handle the case where a user with this email already exists
        if Users.objects.filter(email=email).exists():
            return HttpResponse('A user with this email already exists.', status=400)

        # Else, create a new user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = make_password(request.POST.get('password'))  # Hash the password
        tenant_id = request.POST.get('tenant')
        tenant = Client.objects.get(id=tenant_id)

        user = Users(first_name=first_name, 
                     last_name=last_name, 
                     email=email, 
                     password=password, 
                     tenant=tenant, 
                     created_on=timezone.now()
                     )
        
        user.save()

        return HttpResponse("<h1>Franzelle: The user was saved in DB</h1>")
    else:
        tenants = Client.objects.all()  # Fetch all tenants for the dropdown
        context = {'tenants': tenants}
        return render(request, 'global_app/add_users.html', context)

def index(request):
    return HttpResponse("<h1>Hello, La Franzella kong makulit! This is the public index</h1>")