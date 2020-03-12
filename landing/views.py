from django.shortcuts import render, redirect

from landing.forms import *
from products.models import *


def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'landing/home.html', locals())


def add(request):
    form = ProductForm(request.POST or None, request.FILES)
    if request.method == "POST" and form.is_valid():
        print(form)
        new_form = form.save()
    return render(request, 'landing/add.html', locals())


def delete(request, id):
    try:
        news_select = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect('landing/home.html')
    news_select.delete()
    return redirect('landing/home.html')
