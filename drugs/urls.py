from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drugs.views import DrugViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'drugs', DrugViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
