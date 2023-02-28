from django.urls import path

from .views import buy_view, order_view, item_view

urlpatterns = [
    path('buy/<item_id>/', buy_view, name='buy'),
    path(r'order/', order_view, name='order'),
    path(r'item/<pk>/', item_view, name='item'),
]
