from django.urls import path
from .views import ReviewCreateView, ReviewListView, ReviewDetailView, ReviewDeleteView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('list/', ReviewListView.as_view(), name='review-list'),
    path('detail/<str:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('delete/<str:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
]

app_name = 'review'
