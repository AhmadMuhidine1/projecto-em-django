from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class mercado(models.Model):
    City = models.CharField(max_length=100)
    Descripions = models.TextField(max_length=250)
    Phone = models.CharField(max_length = 15)
    Email = models.EmailField()
    Photo = models.ImageField()
    Activa = models.BooleanField(default=True)
    Begin_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    class meta:
        db_table = 'mercado'