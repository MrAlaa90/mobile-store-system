from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, CustomerViewSet, SaleViewSet, RepairViewSet
from .sync_views import BatchSyncView
from .license_views import GenerateLicenseView

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'repairs', RepairViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sync/', BatchSyncView.as_view(), name='batch-sync'),
    path('license/generate/', GenerateLicenseView.as_view(), name='license-generate'),
]
