from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, CustomerViewSet, SaleViewSet, RepairViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'repairs', RepairViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
