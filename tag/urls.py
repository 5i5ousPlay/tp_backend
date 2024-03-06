from django.urls import path
from .views import TagCreateView, TagListView, TagDetailView, TagDeleteView

urlpatterns = [
    path('create/', TagCreateView.as_view(), name='tag-create'),
    path('list/', TagListView.as_view(), name='tag-list'),
    path('detail/<str:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('delete/<str:pk>/', TagDeleteView.as_view(), name='tag-delete'),
]

app_name = 'tag'
