from django.urls import path

from . import views

# use the view classes by calling as_view() on the class (derived from APIView).
urlpatterns = [
    path('', views.api_root),
    path('warehouse/', views.WarehouseList.as_view(), name='warehouse-list'),
    path('warehouse/<int:pk>', views.WarehouseSingle.as_view(), name='warehouse-single'),
    path('item/', views.ItemList.as_view(), name='item-list'),
    path('item/<int:pk>', views.ItemSingle.as_view(), name='item-single'),
]
