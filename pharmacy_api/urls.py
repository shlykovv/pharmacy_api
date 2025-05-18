from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet


router = DefaultRouter()
router.register(OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drugs.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
]

urlpatterns += router
