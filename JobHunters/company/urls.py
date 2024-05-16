from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # localhost:8000/jobs
    path('', views.index, name='company-index'),
    path('delete_company/<int:id>', views.delete_company, name='delete-company'),
    path('update_company/<int:id>', views.update_company, name='update-company'),
    path('<int:id>', views.get_company_by_id, name='get-company'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)