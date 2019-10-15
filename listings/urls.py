from django.urls import path
from .views import ListingsView
urlpatterns=[
    path('generics/listings/',ListingsView.as_view()),
    path('generics/listings/<int:id>/',ListingsView.as_view())
]