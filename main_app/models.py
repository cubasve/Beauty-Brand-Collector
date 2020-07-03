from django.db import models
from django.urls import reverse

CATEGORY = (('S', 'Skincare'), ('M', 'Makeup'), ('A', 'Accessory'))


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
    date = models.DateField('purchase date')
    item = models.CharField(max_length=1,
                            choices=CATEGORY,
                            default=CATEGORY[0][0])

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_item_display()} on {self.date}"