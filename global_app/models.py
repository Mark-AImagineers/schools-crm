from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100,default=False)
    paid_until = models.DateTimeField(null=True, blank=True)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    auto_create_schema = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass

class Users(models.Model):
    first_name = models.CharField(max_length=100,default=False)
    last_name = models.CharField(max_length=100,default=False)
    email = models.CharField(max_length=100,default=False)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='users')
    password = models.CharField(max_length=100,default=False)
    created_on = models.DateTimeField(auto_now_add=False, default=timezone.now)

    def save(self, *args, **kwargs):
        # Hash the password only if it's a new instance or the password has been changed.
        if not self.pk or 'password' in kwargs.get('update_fields', []):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)