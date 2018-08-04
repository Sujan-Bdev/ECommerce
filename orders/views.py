from django.shortcuts import render
from django.db.models import Count

from .models import OrderItem
from backend.models import Book
from .forms import OrderCreateForm
from cart.cart import Cart
from django.db.models import Count

def order_completed(request,id):
    if Book.objects.get(id=id).stock>1:
        Book.objects.get(id=id).stock-=1
    else:
        Book.objects.get(id=id).stock=0


def get_book_order_maximum():
    books=Book.objects.annotate(num_books=Count('order_items')).order_by('-num_books')
    top_10_books = books.exclude(num_books__lt=1)[:9]
    return top_10_books

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
                order.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        book=item['book'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                cart.clear()
            else:
                return render(request, 'sample.html')

        return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form})

# Create your views here.
