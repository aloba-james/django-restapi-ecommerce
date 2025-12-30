from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            # 'description',
            'price',
            'stock',
        )
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "price must be greater thsan 0."
            )
        return value
    
class OrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'quantity'
        )   

class OrderSerializer(serializers.ModelSerializer):
    items = OrderitemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'created_at',
            'status',
            'items'
        )
        

