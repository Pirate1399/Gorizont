from django.db import models


class People(models.Model):
    name = models.CharField(max_length=18)
    job = models.CharField(max_length=20)
    title_foto_148x198 = models.ImageField(upload_to='static/images/about', null=True, blank=True)
    foto_100x134 = models.ImageField(upload_to='static/images/about', null=True, blank=True)
    vk = models.CharField(max_length=500)
    skill_1 = models.CharField(max_length=50)
    skill_2 = models.CharField(max_length=50)
    skill_3 = models.CharField(max_length=50)
    skill_4 = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


