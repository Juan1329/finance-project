from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, CobrancaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'finance', CobrancaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
