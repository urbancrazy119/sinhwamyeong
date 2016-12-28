# coding: utf-8

from __future__ import unicode_literals
from django import forms
from sales.models import day 

ACCEPTABLE_FORMAT = [  '%Y/%m/%d',
                       '%Y%m%d'] 

class SalesEditForm(forms.ModelForm):
    pan_date = forms.DateField(input_formats=ACCEPTABLE_FORMAT)
    class Meta:
        model = day
        fields = ('pan_date','pan_price','pan_type',)


