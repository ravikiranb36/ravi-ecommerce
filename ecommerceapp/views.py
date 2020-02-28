from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')
def shop(request):
    return render(request,'shop.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def product_details(request):
    return render(request,'product-details.html')

