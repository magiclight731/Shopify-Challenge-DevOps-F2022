from rest_framework import serializers
from .models import Warehouse, Item


# serializers convert models to JSON format
class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Warehouses
    Convert each field of the model into a serializer field
    extends the HyperlinkedModelSerializer 'default' class
    """

    # hyperlink stuff
    items_at_warehouse = serializers.HyperlinkedRelatedField(
        many=True, queryset=Item.objects.all(), view_name='item-single'
    )
    url = serializers.HyperlinkedIdentityField(view_name='warehouse-single')

    # default stuff
    class Meta:
        model = Warehouse
        fields = ['url', 'id', 'name', 'items_at_warehouse']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Items
    Convert each field of the model into a serializer field
    extends the HyperlinkedModelSerializer 'default' class
    """

    # hyperlink stuff
    location = serializers.HyperlinkedRelatedField(
        allow_null=True, queryset=Warehouse.objects.all(), view_name='warehouse-single'
    )
    url = serializers.HyperlinkedIdentityField(view_name='item-single')

    # default stuff
    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'arrival_date', 'location']

