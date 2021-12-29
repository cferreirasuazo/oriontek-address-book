from django.urls import path, include
app_name = 'address_book'
from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('add_address/', views.add_address, name="add-address"),
    path('show_addresses/', views.show_addresses, name="show-addresses"),
    path('<int:address_id>/update', views.update_address, name="update-address"),
    path('<int:address_id>/delete', views.delete_address, name="delete-address")
]
