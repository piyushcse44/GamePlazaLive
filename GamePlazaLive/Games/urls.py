from django.urls import path
from .views import homepage,browse,streams,search


urlpatterns = [
    path('',homepage,name="homepage"),
    path('browse',browse,name="browse"),
    path('streams',streams,name="streams"),
    path('search',search,name="search"),
    
]
