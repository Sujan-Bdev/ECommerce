from django.conf.urls import url
from django.urls import path

from backend.views import SampleView, book_list_view, BookDetailSlugView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/',auth_views.login,name='login'),
    path('logout/',auth_views.logout,{'next_page':'/'},name='logout'),
    path('signup',views.CustomerSignUpView.as_view(),name='signup_customer'),
    path('signup/staff',views.StaffSignUpView.as_view(),name='signup_admin'),
]