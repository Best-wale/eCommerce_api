from rest_framework import serializers
from .models import Category, Product,Cart,CartItem
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','timestamp','descr','image']

class CategorySerializer(serializers.ModelSerializer):
    contents = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id','category_name','contents']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('__all__')

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ('__all__')


