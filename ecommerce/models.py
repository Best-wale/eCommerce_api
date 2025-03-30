from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	category_name = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.category_name}"


class Product(models.Model):
	category = models.ManyToManyField(Category, related_name='contents')
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2) 
	descr = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images/')
		
	def __str__(self):
		return f'{self.name}:{self.price}'

class Cart(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order for {self.user.username}"