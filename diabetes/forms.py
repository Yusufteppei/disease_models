from django.forms import ModelForm, Form
from .models import *
from django import forms


class DiabetesTestForm(ModelForm):
    class Meta:
        model = Test
        exclude = ('outcome',)


class BMIForm(Form):
    height = forms.IntegerField(label='Height(cm)')
    weight = forms.IntegerField(label='Weight(kg)')
