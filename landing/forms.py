from django import forms
from landing.models import Subscriber
from products.models import Product


# class SubscribeForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber
#         exclude = [" "]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'short_description', 'description', 'image', 'price']