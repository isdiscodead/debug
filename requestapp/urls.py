from django.urls import path

from requestapp.views import RequestUpdateView, RequestDeleteView, RequestListView, RequestCreateView

app_name = "requestapp"

urlpatterns = [
    path('create/', RequestCreateView.as_view(), name='create'),
    path('list/', RequestListView.as_view(), name='list'),
    path('update/', RequestUpdateView.as_view(), name='update'),
    path('delete/', RequestDeleteView.as_view(), name='delete'),
]
