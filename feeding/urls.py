from django.urls import path
from .views import FeedCreateView, FeedDeleteView, FeedListView

urlpatterns = [
    path('', FeedListView.as_view(), name='feed_list'),
    path('create/', FeedCreateView.as_view(), name='feed_create'),
    path('<int:pk>/delete/', FeedDeleteView.as_view(), name='feed_delete'),
]