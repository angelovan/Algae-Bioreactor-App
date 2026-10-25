from django.urls import path
from . import views

urlpatterns = [
    path('', views.BioreactorListView.as_view(), name='bioreactor_list'),
    path('create/', views.BioreactorCreateView.as_view(), name='bioreactor_create'),
    path('<int:pk>/', views.BioreactorDetailView.as_view(), name='bioreactor_detail'),
    path('<int:pk>/update/', views.BioreactorUpdateView.as_view(), name='bioreactor_update'),
    path('<int:pk>/delete/', views.BioreactorDeleteView.as_view(), name='bioreactor_delete'),
]