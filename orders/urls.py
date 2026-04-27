from django.urls import path
from .views import create_order, user_orders

app_name = 'orders'

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('my-orders/', user_orders, name='user_orders'),
]