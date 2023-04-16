from django.db import models

class Level(models.Model):
    tour_level = models.CharField(max_length=15)

    def __str__(self):
        return self.tour_level

class Tour(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    type_choise = (("Зимний", "Зимний"), ("Летний", "Летний"), ("Всесезонный", "Всесезонный"))
    type = models.CharField(max_length=20, choices=type_choise, default=("Всесезонный", "Всесезонный"))
    location_choise = (("m", "Иркутск, Иркутская область"), ("rf", "Россия"), ("zg", "Заграничный тур"))
    location = models.CharField(max_length=20, choices=location_choise, default=("m", "Иркутск, Иркутская область"))
    pro_gor = models.BooleanField()
    description = models.CharField(max_length=335)
    title_foto = models.ImageField(upload_to='static/images/tour', null=True, blank=True, default='http://placehold.it/460x460')
    file = models.FileField(upload_to='static/files', null=True)
    text = models.TextField()
    priority = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}, {self.priority}"


class Calendar(models.Model):
    name = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return str(self.name)


class Excursion(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    foto = models.ImageField(upload_to='static/images/excursions', null=True, blank=True, default='http://placehold.it/460x460')
    description = models.TextField()
    priority = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} {self.priority}"