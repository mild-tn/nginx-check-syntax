from django.db import models

# Create your models here.
class Redirection(models.Model):
    domain = models.CharField(max_length=250)
    rule = models.CharField(max_length=250)
    redirect_to = models.CharField(max_length=250)
    is_permanent = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_http_to_https = models.BooleanField(default=False)


