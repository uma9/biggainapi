from django.db import models

# Create your models here.


class Categories(models.Model):
     categorie =models.CharField(max_length=150 ,null=True,blank=True)
     subcategorie1=models.CharField(max_length=150,null=True,blank=True)
     subcategorie2=models.CharField(max_length=150,null=True,blank=True)
     subcategorie3=models.CharField(max_length=150,null=True,blank=True)
     subcategorie4=models.CharField(max_length=150,null=True,blank=True)
     subcategorie5=models.CharField(max_length=150,null=True,blank=True)
