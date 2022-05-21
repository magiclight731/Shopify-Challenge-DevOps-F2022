from django.urls import path

from . import views

# use the view classes by calling as_view() on the class (derived from APIView).
urlpatterns = [
    path('warehouse/', views.WarehouseList.as_view()),
    path('warehouse/<int:pk>', views.WarehouseSingle.as_view()),
    path('item/', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemSingle.as_view()),
]
