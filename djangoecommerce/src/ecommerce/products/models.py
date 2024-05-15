from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='static/uploads', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name