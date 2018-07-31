from django.urls import path

from backend import views
from .views import SearchBookListView
urlpatterns = [
    path('', SearchBookListView.as_view(), name='search-list'),

]
