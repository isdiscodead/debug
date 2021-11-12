from django.urls import path


from settingapp.views import option

app_name = "settingapp"

urlpatterns = [
    path('', option, name='option'),

]
