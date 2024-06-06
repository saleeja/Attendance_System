from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('workers/', WorkerCreateView.as_view(), name='worker-create'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('workers/list/', WorkerList.as_view(), name='worker-list'),
]