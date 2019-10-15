from django.db import models
from usermanagement.models import User

# Create your models here.
class Contacts(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone1=models.IntegerField()
    phone2=models.IntegerField()
    Website=models.CharField(max_length=30)
    street1=models.CharField(max_length=30)
    street2=models.CharField(max_length=30)
    nearBy=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    social_info=models.CharField(max_length=30)