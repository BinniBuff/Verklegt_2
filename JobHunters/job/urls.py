from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/jobs
    path('', views.index, name='job-index'),
    path('<int:id>', views.get_job_by_id, name='get-job'),
]