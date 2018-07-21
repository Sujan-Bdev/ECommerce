# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from .models import Book


def home(request):
    # boards = Board.objects.all()
    return render(request, 'home.html')


class SampleView(TemplateView):
    template_name = 'sample.html'


def book_list_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    queryset = Book.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'book_list_view.html', context)


def book_detail_view(request, pk=None, *args, **kwargs):
    # instance = Book.objects.get(pk=pk)
    instance = get_object_or_404(Book, pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'book_detail_view.html', context)


class BookDetailSlugView(DetailView):
    # queryset = Book.objects.all()
    # template_name = 'book_detail_slug_view.html'

    def get(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            data = get_object_or_404(Book, slug=slug)
        except Book.DoesNotExist:
            raise Http404("Not Found!!!")
        except Book.MultipleObjectsReturned:
            queryset = Book.objects.filter(slug=slug)
            data = queryset.first()
        return render(request, 'book_detail_slug_view.html', {
            'book': data
        })


'''
class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book_list_view.html'
'''
