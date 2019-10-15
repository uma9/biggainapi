from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models import Q
from django.db.models.signals import pre_save,post_save

from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
import random
import os
import requests
#from usermanagement.models import User


# Create your models here.
class UserManager(BaseUserManager):
   # use_in_migrations = True

   def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False):
       if not phone:
           raise ValueError('phone must be set!')
       if not password:
           raise ValueError('password must be set')

       user_obj = self.model(
           phone=phone
       )
       user_obj.set_password(password)
       user_obj.staff = is_staff
       user_obj.active = is_active
       user_obj.admin = is_admin
       user_obj.save(using=self._db)
       return user_obj

   def create_staffuser(self, phone, password=None):
       user = self.create_user(
           phone,
           password=password,
           is_staff=True

       )
       return user

   def create_superuser(self, phone, password=None):
       user = self.create_user(
           phone,
           password=password,
           is_admin=True,
           is_staff=True
       )

       return user




class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="phone number must be enterered ")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    user_id = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    email_id = models.EmailField(('email address'))
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_advartiser = models.BooleanField(default=False)
    is_shopinguser=models.BooleanField(default=False)
    is_subscriber=models.BooleanField(default=False)
    is_vendor=models.BooleanField(default=False)
    #is_superuser=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    first_login = models.BooleanField(default=False)
    date_of_Birth=models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'phone'
   # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def get_full_name(self):
        if self.name:
            return self.name
        else:
            return self.phone

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_avtive(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

class PhoneOTP(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="phone number must be enterered ")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    otp=models.CharField(max_length=9,blank=True,null=True)
    count=models.IntegerField(default=0,help_text='number of otps sent')
    validated=models.BooleanField(default=False,help_text='if it is true ,that means user have validate otp correctly in second api')
    def __str__(self):
        return str(self.phone)+'is sent'+str(self.otp)