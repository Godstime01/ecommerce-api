from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.DecimalField(decimal_places=1, default=0, max_digits=3)
    count = models.IntegerField(default=0)
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)

    def __str__(self): return self.rating