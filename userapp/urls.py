from django.urls import path
from userapp.views import *

from userapp.views import UserCreateView

app_name = "userapp"

urlpatterns = [
    path('login/', login_check, name='login'),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup")
]