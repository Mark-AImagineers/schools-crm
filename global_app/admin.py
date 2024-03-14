from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Client)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'get_tenant_name')

    def get_tenant_name(self, obj):
        return obj.tenant.name
    get_tenant_name.short_description = 'Client Name'