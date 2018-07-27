from django.conf.urls import url
from django.urls import path

from backend.views import SampleView, book_list_view, BookDetailSlugView
from . import views

urlpatterns = [
    path('',views.admin_panel,name='eadmin'),
    path('book/add',views.AddBook,name='add_book'),
    path('book/add/<int:pk>',views.AddAuthor,name='add_book_author')

]