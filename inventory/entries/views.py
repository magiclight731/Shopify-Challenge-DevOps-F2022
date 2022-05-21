from .models import Warehouse, Item
from .serializers import WarehouseSerializer, ItemSerializer
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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


@api_view(['GET'])  # users can only make GET requests for the following
def api_root(request):
    """
    'root' endpoint view of our API.
    Since this is a one-off and only needs GET access, we use a function setup to reduce complexity,
    instead of a class setup to reduce code reuse, as was done above.
    :param request: the HTTP request calling this
    :return: links to the item-list and warehouse-list endpoints on whatever server is running
    """
    return Response({
        'items': reverse('item-list', request=request),
        'warehouses': reverse('warehouse-list', request=request)
    })
