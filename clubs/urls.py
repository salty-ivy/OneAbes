from django.urls import path
from . views import *

app_name = 'clubs'

urlpatterns = [
    path('', clubView, name='club-view'),
]