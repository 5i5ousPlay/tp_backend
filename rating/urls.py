from django.urls import path
from .views import RatingCreateView, RatingListView, RatingDetailView, RatingDeleteView

urlpatterns = [
    path('create/', RatingCreateView.as_view(), name='rating-create'),
    path('list/', RatingListView.as_view(), name='rating-list'),
    path('detail/<str:pk>/', RatingDetailView.as_view(), name='rating-detail'),
    path('delete/<str:pk>/', RatingDeleteView.as_view(), name='rating-delete'),
]

app_name = 'rating'
