from django.urls import path
from .views import homepage,browse,streams,search
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',homepage,name="homepage"),
    path('browse/',browse,name="browse"),
    path('streams/',streams,name="streams"),
    path('search/',search,name="search"),
    
]
