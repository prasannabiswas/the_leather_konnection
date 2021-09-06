from django.db import models

class Bag(models.Model):
    title = models.CharField(max_length=100)
    id_no = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/products/images/')
    description = models.CharField(max_length=200)


