from django.urls import path
from .views import BuildingCreateView, BuildingListView, BuildingDetailView, BuildingDeleteView

urlpatterns = [
    path('create/', BuildingCreateView.as_view(), name='building-create'),
    path('list/', BuildingListView.as_view(), name='building-list'),
    path('detail/<str:pk>/', BuildingDetailView.as_view(), name='building-detail'),
    path('delete/<str:pk>/', BuildingDeleteView.as_view(), name='building-delete'),
]

app_name = 'building'
