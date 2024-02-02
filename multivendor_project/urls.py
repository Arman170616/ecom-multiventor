from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.views import CustomUserViewSet, ProductViewSet, CartItemViewSet, CartViewSet, OrderViewSet, DailyDataViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dailydata', DailyDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

