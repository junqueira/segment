# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

ROOM_TPYE_CHOICES=(
    ('standard','padrão'),
    ('better','melhor'),
    ('president','presidente')
)

ORDER_STATE_CHOICES=(
    ('will','liberado'),
    ('run','ocupado'),
    ('end','fim'),
    ('destroyed','destruído'),
)


class Hotel(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    address = models.CharField(max_length=50)
    description = models.TextField()


class Customer(models.Model):
    tel = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    cardid=models.IntegerField(null=True,blank=True)

class RoomInfo(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    price = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Order(models.Model):
    #id
    name = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    cardid = models.CharField(max_length=45)
    roomtype = models.CharField(max_length=45,choices= ROOM_TPYE_CHOICES)
    begin = models.DateField()
    end = models.DateField()
    totalprice = models.IntegerField()
    state=models.CharField(max_length=45,choices=ORDER_STATE_CHOICES)




