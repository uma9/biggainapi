from rest_framework import viewsets
from .serializer  import categoriesserializers
from categories.models import Categories
from rest_framework.views import APIView
from django.contrib import messages, auth


class CategorieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all()
    serializer_class = categoriesserializers

