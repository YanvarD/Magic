from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    categoty_name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.name
    
    
