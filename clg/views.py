from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django app!")
