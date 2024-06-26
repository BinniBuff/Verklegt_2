from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='job-index'),
    path('<int:id>', views.get_job_by_id, name='get-job'),
    path('create_job', views.create_job, name='create-job'),
    path('delete_job/<int:id>', views.delete_job, name='delete-job'),
    path('update_job/<int:id>', views.update_job, name='update-job'),
    path('applications/', views.user_applications, name='user_applications'),
]
