from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/step1/', views.apply_step_1, name='apply_step_1'),
    path('apply/<int:job_id>/step2/', views.apply_step_2, name='apply_step_2'),
    path('apply/<int:job_id>/step3/', views.apply_step_3, name='apply_step_3'),
    path('apply/<int:job_id>/step4/', views.apply_step_4, name='apply_step_4'),
    path('apply/<int:job_id>/status/', views.application_status, name='application_status'),
    path('apply/success/', views.application_success, name='application_success'),
]
