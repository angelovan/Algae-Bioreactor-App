from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.ObservationDashboardView.as_view(),
        name='observation_dashboard',
    ),
    path('log/create/', views.LogCreateView.as_view(), name='log_create'),
]