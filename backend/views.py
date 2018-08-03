# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, FormView
from django.core.paginator import Paginator

from NewBook.models import UpcomingBook
from cart.forms import CartAddBookForm
from .models import Book, Category
from orders.models import OrderItem, Order
from recommendation.main import recommend


class HomeView(TemplateView):
    # queryset = Book.objects.all()
    # template_name = 'book_detail_slug_view.html'

    def get(self, request, *args, **kwargs):
        customer_book = []
        recommend_book = []
        n = 0
        books = Book.objects.all()
        if request.user.is_authenticated:
            user = request.user.username
            user_info = User.objects.get(username=user)
            id_no = user_info.id
            customer_order = Order.objects.all().filter(user=id_no)
            if len(customer_order):
                for order in customer_order:
                    order_id = order.id
                    customer_info = OrderItem.objects.get(order_id=order_id)
                    customer_book.append(customer_info.book)
                index = recommend(customer_book, books)
                for i in index:
                    recommend_book.append(Book.objects.get(id=i))
                recommend_book = (filter(lambda x: x not in customer_book, recommend_book))
                n = len(index) - len(customer_book)
        category = Category.objects.all()
        pagination = Paginator(books, 2)
        page = request.GET.get('page')
        book_list = pagination.get_page(page)
        upcomingbook = UpcomingBook.objects.all()
        print(upcomingbook)
        context = {
            'object_list': book_list,
            'categories': category,
            'recommend': recommend_book,
            'length': n,
            'upcomingbook': upcomingbook
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
    print(request.user.username)
    context = {
        'object_list': queryset,
    }
    return render(request, 'book_list_view.html', context)


def book_detail_view(request, pk=None, *args, **kwargs):
    # instance = Book.objects.get(pk=pk)
    instance = get_object_or_404(Book, pk=pk)
    cart_book_form = CartAddBookForm(id=pk)
    context = {
        'object': instance,
        'cart_book_form': cart_book_form
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
            cart_book_form = CartAddBookForm(id=data.id)
        except Book.DoesNotExist:
            raise Http404("Not Found!!!")
        except Book.MultipleObjectsReturned:
            queryset = Book.objects.filter(slug=slug)
            data = queryset.first()
            cart_book_form = CartAddBookForm(id=data.id)
        return render(request, 'book_detail_slug_view.html', {
            'book': data,
            'cart_book_form': cart_book_form
        })


def CategorySlugView(request, slug):
    book_list = Book.objects.filter(category__slug=slug)
    category = Category.objects.all()
    return render(request, 'category_view.html', {'object_list': book_list, 'categories': category})
