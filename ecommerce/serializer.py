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

#class CartSerializer(serializers.ModelSerializer):

  #  class Meta:
  #      model = Cart
   #     fields = ('__all__')
#class AllSerializer(serializers.ModelSerializer):
#    cart = CartSerializer(many=True)
#    cate = CategorySerializer(many=True)
 #   class Meta:
  #      fields = ['cart','cate']


