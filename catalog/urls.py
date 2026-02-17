from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductDetailView, ProductListView, ProductCreateView, ContactView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', ProductListView.as_view(), name='products_list'),

    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products_list/', ProductListView.as_view(), name='products_list'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),

    path('contacts/', ContactView.as_view(), name='contacts'),

]
