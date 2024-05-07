from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/companies
    path('', views.index, name='company-index'),
]