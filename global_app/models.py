from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.contrib.auth.models import User
User = get_user_model()

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']