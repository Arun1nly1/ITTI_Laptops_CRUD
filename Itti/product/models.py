# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.CharField(max_length = 20)
    pname = models.CharField(max_length = 100)
    pprice = models.IntegerField()
    class Meta:
        db_table = "products"
