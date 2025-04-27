# lostitems/urls.py

from django.urls import path
from .views import (
    LostItemListView, 
    LostItemDetailView, 
    LostItemCreateView,
    home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', LostItemCreateView.as_view(), name='lost_item_register'),
    path('lost-items/', LostItemListView.as_view(), name='lost_item_list'),
    path('lost-items/<int:pk>/', LostItemDetailView.as_view(), name='lost_item_detail'),
]