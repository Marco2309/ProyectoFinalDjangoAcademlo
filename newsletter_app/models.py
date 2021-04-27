from django.db import models
from tags_app.models import Tag
from django.contrib.auth.models import User


class Newsletters(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='imagenes', null=True)
    target = models.IntegerField()
    frecuencia = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name='newsletters')
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
