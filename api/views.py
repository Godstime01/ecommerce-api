from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import ProductSerializer, UserSerializers, CategorySerializers
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RegistrationView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = UserSerializers


class CategoryView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    lookup_field = 'name'
