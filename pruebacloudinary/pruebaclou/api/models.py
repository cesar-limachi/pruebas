from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Hoteles(models.Model):
    hotel = models.CharField(max_length=100)
    #Imagen = models.ImageField(upload_to='hoteles', blank=True,null=True)
    imagen = CloudinaryField('image',default='')

    def __str__(self):
        return self.hotel