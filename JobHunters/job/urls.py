from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/jobs
    path('', views.index, name='index'),
]