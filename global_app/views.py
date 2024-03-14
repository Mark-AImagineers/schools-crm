from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

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
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'global_app/add_users.html', context)

def index(request): ##the index page is the user login page
    if request.method == "POST":
        email_address = request.POST.get('email_address')
        password = request.POST.get('password').strip()

        print(f"Attempting login with email: {email_address}")
        
        
        print(f"The password in the db {password}")

        try:
            user = Users.objects.get(email=email_address)

            print(f"User found in DB: {user.email}")
            print(f"the password that the user input is: {password}")
            print(f"The password when hashed is CODED: {make_password(password)}")
            print(f"Hashed password from DB: {user.password}")

            if check_password(password, user.password):
                return HttpResponse("Logged in successfully! Redirect me to Tenant Screen")
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=400)
        except Users.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist'}, status=404)
    else:
        return render(request, 'global_app/signin.html')