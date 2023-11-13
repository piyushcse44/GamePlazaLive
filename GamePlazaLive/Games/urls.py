from django.urls import path
from .views import homepage,browse,streams


urlpatterns = [
    path('',homepage,name="homepage"),
    path('browse/',browse,name="browse"),
    path('streams/',streams,name="streams"),
    
]
