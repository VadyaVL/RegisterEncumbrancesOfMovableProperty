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
        fields = [
            'Country',
            'Index',
            'Region',
            'Area',
            'City',
            'Street',
            'Home',
        ]



class EncumbranceForm(ModelForm):
    class Meta:
        model = Encumbrance
        fields = [
            'NStatement',
            'DateStatement',
            'TypeOfEncumbrance',
            'ViewEncumbrance',
            'TypeReg',
            'AddedInfo',
            'WPerson',
            'SPerson',
        ]

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'Identification',
            'NonResidentForeigner',
            'Name',
            'MoreInformation',
            'Address',
        ]

class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = [
        'Name',
        'SerialNumber',
        'RegNumber',
        'AddedInfoForUNMovable',
        ]

class DocumentForm(ModelForm):
    class Meta:
        model = DocumentBase
        fields = [
            'Name',
            'Number',
            'Date',
            'PublisherName',
        ]

class TermForm(ModelForm):
    class Meta:
        model = Terms
        fields = [
            'SizeObligations',
            'LimitDate',
            'AddedInfo',
            'TypeOfCurrency',
        ]