from django.db import models

# Create your models here.
class Add_apis(models.Model):
    apisl = models.IntegerField()
    apikey = models.CharField(max_length=50)
    api_value = models.CharField(max_length=50)
    api_details = models.CharField(max_length=200)
    api_url = models.URLField
    api_type = models.CharField(max_length=15)
    request_body = models.CharField(max_length=300)