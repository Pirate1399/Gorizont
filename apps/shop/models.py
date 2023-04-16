from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    choise = (("ts", "Футболка"), ("sh", "Шеврон"), ("t", "Толстовка"), ("ot", "Остальное"))
    product_type = models.CharField(max_length=200, choices=choise, default=("ot", "Остальное"))
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    description = models.TextField(max_length=550)
    title_foto = models.ImageField(upload_to='static/images/shop/products', null=True, blank=True, default='http://placehold.it/160x160')
    detals = models.TextField()
    priority = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} {self.priority}"


class ProductImage(models.Model):
    name = models.ForeignKey(Product, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='static/images/shop/products', blank=True)

    def __str__(self):
        return str(self.name)