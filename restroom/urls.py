from django.urls import path
from .views import RestroomCreateView, RestroomListView, RestroomDetailView, RestroomDeleteView

urlpatterns = [
    path('create/', RestroomCreateView.as_view(), name='restroom-create'),
    path('list/', RestroomListView.as_view(), name='restroom-list'),
    path('detail/<str:pk>/', RestroomDetailView.as_view(), name='restroom-detail'),
    path('delete/<str:pk>/', RestroomDeleteView.as_view(), name='restroom-delete'),
]

app_name = 'restroom'
