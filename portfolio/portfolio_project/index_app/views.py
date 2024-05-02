from django.shortcuts import render

# Create your views here.

def indexPage_(request):
    return render(request, 'frontend/index.html')