from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply')
]
