#listings app URL Configuration
from django.urls import path
from . import views
urlpatterns = [
    path('listings/', views.ListingList.as_view(), name='listing-list'),
]