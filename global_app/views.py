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

def index(request):
    return HttpResponse("<h1>Hello, La Franzella kong makulit! This is the public index</h1>")