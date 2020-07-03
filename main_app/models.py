from django.db import models
from django.urls import reverse


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    founded = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'brand_id': self.id})


class Purchase(models.Model):
    date = models.DateField()
    item = models.CharField(max_length=100)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item} on {self.date}"