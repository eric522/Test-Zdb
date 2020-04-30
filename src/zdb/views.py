from django.views.generic import ListView
from .models import Movie

# Create your views here.
class ZdbListView(ListView):
    template_name = 'zdb/zdb.html'
    model = Movie
    context_object_name = 'movies'

class ZdbSearchListView(ListView):
    template_name = 'zdb/zdb-search.html'
    model = Movie
    context_object_name = 'results'

    def get_queryset(self):
        query_search = self.request.GET.get('query_search')
        if query_search != '':
            return Movie.objects.filter(title__contains=query_search)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_search'] = self.request.GET.get('query_search')
        return context