from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.hashers import make_password

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=255,default=False)
    paid_until = models.DateTimeField(null=True, blank=True)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    auto_create_schema = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass