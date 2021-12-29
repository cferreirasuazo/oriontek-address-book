from django.db import models
from django.contrib.auth.models import User
class Address(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255) 
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    country_province = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    country = models.TextField()
    details = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.id