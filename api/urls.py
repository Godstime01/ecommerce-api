from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegistrationView, CategoryView


router = DefaultRouter()
router.register(r"products", ProductViewSet, basename='products')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegistrationView.as_view(), name="register"),
    path("products/category/", CategoryView.as_view()),
    path("", include(router.urls))
]