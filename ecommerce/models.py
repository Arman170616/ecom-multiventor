from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone





class CustomUser(AbstractUser):
    USER_TYPES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='buyer')
    user_groups = models.ManyToManyField(Group, related_name='ecommerce_users', blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def is_emply(self):
        return not self.cart_items.exists()
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return self.product.price * self.quantity
    

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='orders')
    items = models.ManyToManyField(CartItem, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def create_order(self):
        cart = self.user.cart
        self.items.set(cart.cart_items.all())
        self.total_amount = sum([item.total_price() for item in self.items.all()])
        self.save()
        cart.cart_items.all().delete()

    def __str__(self):
        return f'Order {self.id}'
    

class DailyData(models.Model):
    date = models.DateField(unique=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    
    @classmethod
    def create_daily_data(cls):
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        orders = Order.objects.filter(created_at__date=yesterday)
        revenue = sum([order.total_amount for order in orders])
        cls.objects.create(date=yesterday, revenue=revenue)

    def __str__(self):
        return f'Daily Data for {self.date} - Revenue: {self.revenue}'

        
        


