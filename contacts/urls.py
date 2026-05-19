from django.urls import path
from .views import contacts_view, subscribe_view

app_name = 'contacts'

urlpatterns = [
    path('', contacts_view, name='contacts'),
    path('subscribe/', subscribe_view, name='subscribe'),
]
