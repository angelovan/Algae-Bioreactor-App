from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import BioreactorUnitForm
from .models import BioreactorUnit

# Create your views here.

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