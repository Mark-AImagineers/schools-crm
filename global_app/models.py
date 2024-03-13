from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=255,default=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Domain(DomainMixin):
    pass


