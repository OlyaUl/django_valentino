from django.db import models

# Create your models here


class Product(models.Model):
    name = models.TextField()
    model = models.TextField(blank=True)
    category = models.TextField()
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    url = models.URLField()
    image = models.TextField()
    site = models.URLField()
    date = models.DateTimeField()
    currency = models.TextField()
    price = models.TextField()
    size = models.TextField(blank=True)
    # sale_price = models.TextField(blank=True)

    def __str__(self):
        return self.name