from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField('Región', max_length=30)

    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        ordering = ['name']
        unique_together = ('name',)
    
    def __str__(self):
        return self.name

class Tipo(models.Model):
    name = models.CharField('Tipos', max_length=30)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['name']
        unique_together = ('name',)
    
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField('Nombre', max_length=30)
    pc = models.IntegerField('PC')
    ps = models.IntegerField('PS')
    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    tipos = models.ManyToManyField(Tipo)
    avatar = models.ImageField(upload_to = 'pokemon', blank = True, null = True)

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Bichos'
        ordering = ['name']
        unique_together = ('name',)
    
    def __str__(self):
        return self.name