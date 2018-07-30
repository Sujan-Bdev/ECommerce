# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, FormView
from django.core.paginator import Paginator
from cart.forms import CartAddBookForm
from .models import Book, Category, Author, BookLinkAuthor

from django.core import paginator


class HomeView(TemplateView):
    # queryset = Book.objects.all()
    # template_name = 'book_detail_slug_view.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        print(books)
        category = Category.objects.all()
        context = {
            'object_list': books,
            'categories': category,

        }
        return render(request, 'index.html', context)


class SampleView(TemplateView):
    template_name = 'home.html'


class TestView(TemplateView):
    template_name = 'static.html'


def book_list_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    queryset = Book.objects.all()
    page = paginator(queryset, 10)

    context = {
        'object_list': queryset,
    }
    return render(request, 'book_list_view.html', context)


def book_detail_view(request, pk=None, *args, **kwargs):
    # instance = Book.objects.get(pk=pk)
    instance = get_object_or_404(Book, pk=pk)
    cart_book_form = CartAddBookForm()
    context = {
        'object': instance,
        'cart_book_form': cart_book_form
    }
    return render(request, 'book_detail_view.html', context)


class BookDetailSlugView(DetailView):
    # queryset = Book.objects.all()
    # template_name = 'book_detail_slug_view.html'
    cart_book_form = CartAddBookForm()

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
            'book': data,
            'cart_book_form': self.cart_book_form
        })


def CategorySlugView(request, slug):
    book_list = Book.objects.filter(category__slug=slug)
    category = Category.objects.all()
    return render(request, 'category_view.html', {'object_list': book_list, 'categories': category})


'''
class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book_list_view.html'
'''
