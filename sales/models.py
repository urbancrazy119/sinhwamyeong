# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class day(models.Model):
	PAN_TYPE = (
		('01','Cash'),
		('02','Credit'),
		('03','Preorder'),
	)
	pan_date = models.DateTimeField(null=False)
	pan_price= models.IntegerField(null=False)
	pan_type = models.CharField(max_length=2, choices=PAN_TYPE, null=False)
	pan_end  = models.CharField(max_length=1, default='N')
