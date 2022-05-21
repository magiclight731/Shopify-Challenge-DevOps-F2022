from rest_framework import serializers
from .models import Warehouse, Item


# serializers convert models to JSON format
class WarehouseSerializer(serializers.ModelSerializer):
    """
    Serializer for Warehouses
    Convert each field of the model into a serializer field
    extends the ModelSerializer 'default' class
    """
    class Meta:
        model = Warehouse
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Items
    Convert each field of the model into a serializer field
    extends the ModelSerializer 'default' class
    """
    class Meta:
        model = Item
        fields = ['id', 'name', 'arrival_date', 'location']

