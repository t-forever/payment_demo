from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request, 'base/home.html')

def payment_success(request):
    messages.success(request, 'Payment Success')
    return render(request, 'base/home.html')

def payment_failure(request):
    messages.error(request, 'Payment Failure')
    return render(request, 'base/home.html')

