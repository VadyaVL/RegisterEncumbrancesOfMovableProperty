__author__ = 'Vadim_Lytvin'

from django.forms import ModelForm
from models import *



class TypeCurrencyForm(ModelForm):
    class Meta:
        model = TypeOfCurrency
        fields = ['Name']

class ViewForm(ModelForm):
    class Meta:
        model = ViewEncumbrance
        fields = ['Name']

class TypeForm(ModelForm):
    class Meta:
        model = TypeOfEncumbrance
        fields = ['Name']

class TypeRegForm(ModelForm):
    class Meta:
        model = TypeReg
        fields = ['Name']

class AddressForm(ModelForm):
    class Meta:
        model = Address

class EncumbranceForm(ModelForm):
    class Meta:
        model = Encumbrance
        fields = [
            'NStatement',
            'TypeOfEncumbrance',
            'ViewEncumbrance',
            'TypeReg',
            'Date',
            'AddedInfo',
            'WPerson',
            'SPerson',
        ]
