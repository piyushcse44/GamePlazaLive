from django.urls import path
from .views import login,signup,logout,profile


urlpatterns = [
   path('login/',login,name="login"),
   path('login/',logout,name="logout"),
   path('signup/',signup,name="signup"),
   path('profile/',profile,name="profile"),
    
]