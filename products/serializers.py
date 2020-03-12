from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView

from .models import *

class productSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'short_description', 'description', 'image', 'price']

