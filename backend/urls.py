from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('sample/', views.sample, name='sample')
]

urlpatterns+=[
    path('signup/customer',views.CustomerSignUpView.as_view(),name='signup_customer'),
    path('signup/staff',views.StaffSignUpView.as_view(),name='signup_admin'),
]
