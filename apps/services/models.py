from django.db import models


class Snaraga(models.Model):
    name = models.CharField(max_length=33)
    price1 = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    price2 = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    foto = models.ImageField(upload_to='static/images/services/products', null=True, blank=True)
    description = models.TextField(max_length=550)
    choise = (("s", "Спальники/палатки"), ("sn", "Снаряжение"), ("p", "прочее"))
    type = models.CharField(max_length=200, choices=choise, default=("p", "прочее"))

    def __str__(self):
        return str(self.name)

# Create your models here.
