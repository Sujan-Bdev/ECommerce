from django.urls import path
from .views import SearchBookListView

urlpatterns = [
    path('', SearchBookListView.as_view(), name='search-list'),
]
