import imp
from django.urls import path
from .views import ItemList, ItemDetail, ItemCreate

urlpatterns = [
    path('', ItemList.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='detail'),
    path('additem/', ItemCreate.as_view(), name='create'),
]
