from django.shortcuts import render


# Create your views here.
def products(request, *args, **kwargs):
    return render(request, 'products/index.html')
