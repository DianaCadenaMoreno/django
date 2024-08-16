from django.db import models
from datetime import datetime

class Type(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    data_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    data_creation = models.DateField(auto_now=True)
    data_updated = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']