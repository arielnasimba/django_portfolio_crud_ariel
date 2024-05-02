from django.shortcuts import render

# Create your views here.


def home_about(request):
    
    return render(request, 'frontend/about.html')