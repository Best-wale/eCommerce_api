from django.contrib import admin
from .models import Category,Product,Category,Cart,CartItem,Order
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    filter_horizontal = ('category',) 


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)