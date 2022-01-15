from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Items(models.Model):
    class HouseNo(models.TextChoices):
        FOUREIGHT = '48', "48 Callodine"
        SIXFIVE = '65', "65 Callodine"
    
    class StoreName(models.TextChoices):
        INDSTORE = 'INDSTORE', "Indian Store"
        TOPS = 'TOPS', "Tops"
        WALMART = 'WALMART', "Walmart"
        OTHERS = 'OTHERS', "Others"

    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    house_no = models.CharField(max_length=7,
                  choices=HouseNo.choices,
                  default=HouseNo.FOUREIGHT)
    store = models.CharField(max_length=25,
                  choices=StoreName.choices,
                  default=StoreName.TOPS)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['complete', 'house_no']

    
    


