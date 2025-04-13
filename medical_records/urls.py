from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_record, view_records, edit_record, delete_record

urlpatterns = [
    path('upload/', upload_record, name='upload_record'),
    path('view/', view_records, name='view_records'),
    path('edit/<int:record_id>/', edit_record, name='edit_record'),
    path('delete/<int:record_id>/', delete_record, name='delete_record'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
