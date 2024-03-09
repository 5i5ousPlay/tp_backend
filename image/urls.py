from django.urls import path
from .views import ImageUploadView, ImageListView, ImageDetailView, ImageDeleteView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload-view'),
    path('list/', ImageListView.as_view(), name='image-list-view'),
    path('detail/<str:pk>/', ImageDetailView.as_view(), name='image-detail-view'),
    path('delete/<str:pk>/', ImageDeleteView.as_view(), name='image-delete-view'),
]
