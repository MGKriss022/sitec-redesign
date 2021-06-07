from django.db import models
from django.contrib.auth.models import User

class SitecUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_updated_at = models.DateTimeField(auto_now=True)
    