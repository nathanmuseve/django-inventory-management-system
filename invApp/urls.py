from django.urls import path
from . import views
#app name
app_name = 'invApp'
#views/path routes

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.product_create_view, name='product_create'),
    path('list', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.update_confirm_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
    path('delete/<int:product_id>/', views.delete_success_view, name='delete_success'),
]
