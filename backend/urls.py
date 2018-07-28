from django.conf.urls import url
from django.urls import path

from backend.views import SampleView, BookDetailSlugView, TestView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', SampleView.as_view(), name='home'),
    path('book/', views.book_list_view, name='book-list'),
    path('test/', TestView.as_view(), name='test'),
    path('book/<int:pk>', views.book_detail_view, name='book-detail'),
    # path('book/<slug:slug>,<int:pk>/', views.book_detail_slug_view, name='slug-detail'),
    url(r'^book/(?P<slug>[\w-]+)/$', BookDetailSlugView.as_view(), name='detail'),

]
