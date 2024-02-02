from django.contrib import admin
from .models import CustomUser, Product, Cart, CartItem, Order

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
# Compare this snippet from ecommerce/views.py: