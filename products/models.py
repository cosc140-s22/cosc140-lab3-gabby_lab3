from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50, blank=False)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, blank=False)
  minimum_age_appropriate = models.IntegerField(blank=False, default=0)
  maximum_age_appropriate = models.IntegerField(blank=False, default=-1)

  def __str__(self):
    return f"{self.id}: {self.name} ${self.price:0.2f}"