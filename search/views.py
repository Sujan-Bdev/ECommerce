from django.db.models import Q
# Create your views here.
from django.views.generic import ListView
from backend.models import Book


class SearchBookListView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchBookListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        method_dict = request.GET
        query = method_dict.get('q')
        print(query)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query)
            return Book.objects.filter(lookups).distinct()
        return Book.objects.none()
