from django.contrib.messages.storage import session
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from products.models import *
from rest_framework import viewsets
from .serializers import productSeralizer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSeralizer

class SingleProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = productSeralizer


def product(request, product_id):
    get_product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())
