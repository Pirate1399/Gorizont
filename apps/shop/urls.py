from django.urls import path
from .views import ShopView, ProructDetails, ProductSort

app_name = 'shop'
urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('type/<product_type>', ProductSort.as_view(), name= 'product_sort'),
    path('<int:product_id>', ProructDetails.as_view(), name = 'product'),
    ]