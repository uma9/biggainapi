from django.shortcuts import render
from rest_framework import generics,mixins
from .serializer import ListingSerializer
from .models import Listings

class ListingsView(generics.GenericAPIView,
                   mixins.ListModelMixin ,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin):
    serializer_class =ListingSerializer
    queryset = Listings.objects.all()
    lookup_field = 'id'
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    def post(self,request):
        return self.create(request)
    def put(self,request, id=None):
        return self.update(request,id)
