from django import forms
from . models import *

DATE_INPT_FORMAT = ('%d-%m-%Y')

class dateForm(forms.Form):
    date = forms.CharField(label='Enter Data')
