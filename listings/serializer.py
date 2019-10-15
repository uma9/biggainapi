from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Listings
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listings
        fields = '__all__'