# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class day(models.Model):
	PAN_TYPE = (
		('01','현금'),
		('02','카드'),
		('03','선주문'),
	)
	pan_date = models.DateTimeField(null=False)
	pan_price= models.IntegerField(null=False)
	pan_type = models.CharField(max_length=2, choices=PAN_TYPE, null=False)
	pan_end  = models.CharField(max_length=1, default='N')
