from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='image')


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__ (self):
        return self.name