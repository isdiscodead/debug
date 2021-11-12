from django.urls import path
<<<<<<< HEAD
=======


>>>>>>> 5abe618f1909b75621abf333c0fda1bb0e57e524
from settingapp.views import option

app_name = "settingapp"

urlpatterns = [
    path('', option, name='option'),

]
