from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),
]
