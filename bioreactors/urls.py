from django.urls import path
from .views import (
    AlgaeSpeciesCreateView,
    AlgaeSpeciesListView,
    BioreactorCreateView,
    BioreactorDeleteView,
    BioreactorDetailView,
    BioreactorListView,
    BioreactorUpdateView,
    EquipmentCreateView,
    EquipmentListView, AlgaeSpeciesDeleteView, EquipmentDeleteView, AlgaeSpeciesUpdateView, EquipmentUpdateView,
)

urlpatterns = [
    path('', BioreactorListView.as_view(), name='bioreactor_list'),
    path('create/', BioreactorCreateView.as_view(), name='bioreactor_create'),
    path('<int:pk>/', BioreactorDetailView.as_view(), name='bioreactor_detail'),
    path('<int:pk>/edit/', BioreactorUpdateView.as_view(), name='bioreactor_update'),
    path('<int:pk>/delete/', BioreactorDeleteView.as_view(), name='bioreactor_delete'),

    path('algae/', AlgaeSpeciesListView.as_view(), name='algae_list'),
    path('algae/create/', AlgaeSpeciesCreateView.as_view(), name='algae_create'),
    path('algae/<int:pk>/edit/', AlgaeSpeciesUpdateView.as_view(), name='algae_update'),
    path('algae/<int:pk>/delete/', AlgaeSpeciesDeleteView.as_view(), name='algae_delete'),

    path('equipment/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/edit/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),
]