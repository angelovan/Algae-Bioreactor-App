from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from .forms import NutrientFeedForm
from .models import NutrientFeed

# Create your views here.

class FeedListView(ListView):
  model = NutrientFeed
  template_name = 'feeding/feed_list.html'
  context_object_name = 'feeds'

class FeedCreateView(CreateView):
  model = NutrientFeed
  form_class = NutrientFeedForm
  template_name = 'feeding/feed_form.html'
  success_url = reverse_lazy('feed_list')

class FeedDeleteView(DeleteView):
  model = NutrientFeed
  template_name = 'feeding/feed_confirm_delete.html'
  success_url = reverse_lazy('feed_list')