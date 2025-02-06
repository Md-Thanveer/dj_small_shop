from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet,BrandViewSet,ProductViewSet,CartViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'products',ProductViewSet,basename='product')
router.register(r'carts',CartViewSet,basename='cart')


urlpatterns = [
    path('', include(router.urls)),
]

