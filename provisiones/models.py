from django.db import models

# Create your models here.


class Provisiones(models.Model):
    provision = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=1)
    comprado = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.provision
