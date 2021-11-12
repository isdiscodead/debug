from django.urls import path



app_name = "userapp"

urlpatterns = [
    path('create/', AccountCreatView.as_view, name='create'),
]