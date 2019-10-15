from rest_framework import serializers
from categories.models import Categories
from django.contrib.auth.models import User, Group


class categoriesserializers(serializers.ModelSerializer):
    class Meta:
         model=Categories
         fields='__all__'

