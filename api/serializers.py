from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Category


User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"

    
class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CategorySerializers(serializers.ModelSerializer):

    products = ProductSerializer(many = True, read_only = True)

    class Meta:
        model = Category
        fields = ( "id", "name", "products")