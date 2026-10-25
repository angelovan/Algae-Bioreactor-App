from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import ExperimentLogForm
from .models import ExperimentLog, NutrientFeed

# Create your views here.

class ObservationDashboardView(ListView):
  model = ExperimentLog
  template_name = 'observations/observation_dashboard.html'
  context_object_name = 'logs'
  ordering = ['-date_recorded']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['feeds'] = NutrientFeed.objects.all()
    return context


class LogCreateView(CreateView):
  model = ExperimentLog
  form_class = ExperimentLogForm
  template_name = 'observations/log_form.html'
  success_url = reverse_lazy('observation_dashboard')