from django.urls import path
from .views import *

urlpatterns = [
    path('input/',process_form )
]