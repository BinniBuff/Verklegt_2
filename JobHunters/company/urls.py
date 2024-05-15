from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/jobs
    path('', views.index, name='company-index'),
    path('delete_job/<int:id>', views.delete_company, name='delete-company'),
    path('update_job/<int:id>', views.update_company, name='update-company'),
]