from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import BioreactorUnitForm, AlgaeSpeciesForm, EquipmentForm
from .models import BioreactorUnit, AlgaeSpecies, Equipment


# Create your views here.

class AlgaeSpeciesListView(ListView):
  model = AlgaeSpecies
  template_name = 'bioreactors/algae_list.html'
  context_object_name = 'algae_list'

class AlgaeSpeciesCreateView(CreateView):
  model = AlgaeSpecies
  form_class = AlgaeSpeciesForm
  template_name = 'bioreactors/algae_form.html'
  success_url = reverse_lazy('algae_list')

class AlgaeSpeciesUpdateView(UpdateView):
  model = AlgaeSpecies
  form_class = AlgaeSpeciesForm
  template_name = 'bioreactors/algae_form.html'
  success_url = reverse_lazy('algae_list')

class AlgaeSpeciesDeleteView(DeleteView):
  model = AlgaeSpecies
  template_name = 'bioreactors/algae_confirm_delete.html'
  success_url = reverse_lazy('algae_list')


class EquipmentListView(ListView):
  model = Equipment
  template_name = 'bioreactors/equipment_list.html'
  context_object_name = 'equipment_list'

class EquipmentCreateView(CreateView):
  model = Equipment
  form_class = EquipmentForm
  template_name = 'bioreactors/equipment_form.html'
  success_url = reverse_lazy('equipment_list')

class EquipmentUpdateView(UpdateView):
  model = Equipment
  form_class = EquipmentForm
  template_name = 'bioreactors/equipment_form.html'
  success_url = reverse_lazy('equipment_list')

class EquipmentDeleteView(DeleteView):
  model = Equipment
  template_name = 'bioreactors/equipment_confirm_delete.html'
  success_url = reverse_lazy('equipment_list')


class BioreactorListView(ListView):
  model = BioreactorUnit
  template_name = 'bioreactors/bioreactor_list.html'
  context_object_name = 'bioreactors'

class BioreactorDetailView(DetailView):
  model = BioreactorUnit
  template_name = 'bioreactors/bioreactor_detail.html'
  context_object_name = 'bioreactor'

class BioreactorCreateView(CreateView):
  model = BioreactorUnit
  form_class = BioreactorUnitForm
  template_name = 'bioreactors/bioreactor_form.html'
  success_url = reverse_lazy('bioreactor_list')

class BioreactorUpdateView(UpdateView):
  model = BioreactorUnit
  form_class = BioreactorUnitForm
  template_name = 'bioreactors/bioreactor_form.html'
  success_url = reverse_lazy('bioreactor_list')

class BioreactorDeleteView(DeleteView):
  model = BioreactorUnit
  template_name = 'bioreactors/bioreactor_confirm_delete.html'
  success_url = reverse_lazy('bioreactor_list')