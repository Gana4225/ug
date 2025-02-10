from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to my Django app!")

urlpatterns = [
    path('', home),  # Root URL
    path('clg/', include('clg.urls')),  # Your 'clg' app
    path('payments/', include('payments.urls')),  # Your 'payments' app
]
