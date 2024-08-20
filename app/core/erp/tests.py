# from django.test import TestCase

# # Create your tests here.
from config.wsgi import * 
from core.erp.models import Type, Employee

import random
from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import Coalesce

from core.erp.models import Sale, DetSale

#listar 

# select * from empleado
# query = Type.objects.all()
# print(query)

# insercion
# t = Type()
# t.name = "Prueba"
# t.save()

# t= Type(names='Prueba2').save()

# edicion

# t = Type.objects.get(pk=1)
# t.names = 'Accioni'
# t.save()

# try:
#     t = Type.objects.get(pk=4)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#     print(e)

# eliminacion
# t = Type.objects.get(pk=4)
# t.delete()

# filtrar
# obj = Type.objects.filter(names__icontains='pre')
# obj = Type.objects.filter(names__startswith='p')
# obj = Type.objects.filter(names__in=['presidente']).count()
# obj = Type.objects.filter(names__in=['presidente']).query
# obj = Type.objects.filter(names__endswith='e').exclude(id=2)
# print(obj)

# for i in Type.objects.filter(names__startswith='p'):
#     print(i.names)

# for i in Type.objects.filter(names__startswith='p')[:2]:
#     print(i.names)    

# obj = Employee.objects.filter(type_id=1)
# obj = Employee.objects.filter(date_created=)

for m in range(0, 6):
    pedids = random.randint(18, 29)
    for d in range(1, pedids):
        vent = Sale()
        vent.cli_id = random.randint(1, 3)
        vent.date_joined = datetime(2020, m + 1, d)
        vent.save()

        food = random.randint(1, 10)

        for i in range(0, food):
            det = DetSale()
            det.sale_id = vent.id
            det.prod_id = random.randint(1, 23)
            det.price = det.prod.pvp
            det.cant = random.randint(1, 4)
            det.subtotal = float(det.price) * det.cant
            det.save()

        vent.subtotal = vent.detsale_set.all().aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
        vent.iva = float(vent.subtotal) * 0.12
        vent.total = float(vent.subtotal) + float(vent.iva)
        vent.save()
print('Terminado')