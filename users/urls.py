from django.urls import path
from .views import *

app_name="users"

urlpatterns = [
    path('view-profile/<str:uid>/',profileView,name="profile-view"),
]
