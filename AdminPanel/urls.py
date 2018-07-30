from django.conf.urls import url
from django.urls import path

from backend.views import SampleView, book_list_view, BookDetailSlugView
from . import views


urlpatterns = [
    path('',views.admin_panel,name='eadmin'),
    path('book/add',views.AddBook,name='add_book'),
    path('orders/',views.orders_view,name='orders_list_admin'),
    path('book/add/<int:pk>',views.AddAuthor,name='add_book_author'),
    path('order/<int:pk>',views.orders_detail,name='order_detail_admin')

]