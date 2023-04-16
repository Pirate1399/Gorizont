from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Product, ProductImage

from apps.home.views import form

class ShopView(View):
    def get(self, request):
        data = list(Product.objects.all())
        data = sorted(data, key=lambda product: product.priority)
        context = {"products": data}
        return render(request, 'shop/shop.html', context)
    def post(self, request):
        return form(request)

class ProructDetails(View):
    def get(self, request, product_id):
        data = get_object_or_404(Product, id=product_id)
        images = list(ProductImage.objects.filter(name=data.id))
        a = data.detals.split("#")
        data.detals = a
        context = {"product": data,
                   "images": images}
        return render(request, 'shop/details_prod.html', context)
    def post(self, request):
        return form(request)

class ProductSort(View):
    def get(self, request, product_type):
        data = list(Product.objects.filter(product_type = product_type))
        context = {"products": data}
        return render(request, 'shop/shop.html', context)
    def post(self, request):
        return form(request)