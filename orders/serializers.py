from rest_framework import serializers

from orders.models import Order, OrderItem
from drugs.models import Drug
from drugs.serializers import DrugSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    drug = DrugSerializer(read_only=True)
    drug_id = serializers.PrimaryKeyRelatedField(
        queryset = Drug.objects.all(), source='drug', write_only=True
    )
    
    class Meta:
        model = OrderItem
        fields = ('id', 'drug', 'drug_id', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    created_at = serializers.DateTimeField(ready_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
