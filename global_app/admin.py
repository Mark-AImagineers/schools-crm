from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Client)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant_id')