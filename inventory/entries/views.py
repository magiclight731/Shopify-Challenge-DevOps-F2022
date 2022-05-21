from .models import Warehouse, Item
from .serializers import WarehouseSerializer, ItemSerializer
from rest_framework import generics, mixins
# View classes. These are mostly constructed using generics and/or mixins,
# which simplify code but may be somewhat harder to understand without prior research.


class WarehouseList(generics.ListCreateAPIView):
    # view class for all Warehouses
    # extends the 'List create API view' class from rest_framework.
    # This abstracts out most standard REST logic, allowing GET/POST on the warehouse list endpoint.

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseSingle(generics.RetrieveUpdateDestroyAPIView):
    # view class for one Warehouse
    # extends the 'Retrieve, Update, and Destroy API view' class from rest_framework.
    # This abstracts out most standard REST logic, allowing GET/PUT/DELETE on the single warehouse endpoint.

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ItemList(generics.ListCreateAPIView):
    # view class for all Items
    # extends the 'List create API view' class from rest_framework.
    # This abstracts out most standard REST logic, allowing GET/POST on the item list endpoint.

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemSingle(generics.RetrieveUpdateDestroyAPIView):
    # view class for one Item
    # extends the 'Retrieve, Update, and Destroy API view' class from rest_framework.
    # This abstracts out most standard REST logic, allowing GET/PUT/DELETE on the single item endpoint.

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
