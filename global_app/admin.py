from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Client)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_name', 'tenant_updated_at')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_name', 'domain_updated_at')