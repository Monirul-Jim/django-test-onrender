from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import ProductViewSet

router = DefaultRouter()
router.register(r'categories', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
