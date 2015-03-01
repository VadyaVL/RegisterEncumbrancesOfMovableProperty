# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
from forms import *

def home(request):
    return render(request, 'home.html')

def add(request):

    args = {}
    args['formE'] = EncumbranceForm

    return render(request, 'addHead.html', args)


#Currency - тип валюти
def vCurrency(request):
    args = {}
    args['list'] = TypeOfCurrency.objects.all()
    args['key'] = 'currency'
    return render(request, 'view.html', args)

def aCurrency(request):

    args = {}
    args['form'] = TypeCurrencyForm

    if request.POST:
        args['form'] = TypeCurrencyForm(request.POST, request.FILES)
        if args['form'].is_valid():
            typeC = args['form'].save(commit=False)
            typeC.save()
            args['list'] = TypeOfCurrency.objects.all()
            args['key'] = 'currency'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dCurrency(request, id=0):

    TypeOfCurrency.objects.get(id=id).delete()
    args = {}
    args['list'] = TypeOfCurrency.objects.all()
    args['key'] = 'currency'
    return render(request, 'view.html', args)

def eCurrency(request, id=0):
    args = {}

    typeOfCurrency = TypeOfCurrency.objects.get(id=id)

    if request.POST:
        args['form'] = TypeCurrencyForm(request.POST)

        if args['form'].is_valid():
            typeOfCurrencyT = args['form'].save(commit=False)
            typeOfCurrency.Name = typeOfCurrencyT.Name
            typeOfCurrency.save()
            args['list'] = TypeOfCurrency.objects.all()
            args['key'] = 'currency'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = TypeCurrencyForm(instance = typeOfCurrency)
    return render(request, 'add.html', args)

#View - вид обтяження
def vView(request):
    args = {}
    args['key'] = 'view'
    args['list'] = ViewEncumbrance.objects.all()
    return render(request, 'view.html', args)

def aView(request):

    args = {}
    args['form'] = ViewForm

    if request.POST:
        args['form'] = ViewForm(request.POST, request.FILES)
        if args['form'].is_valid():
            viewC = args['form'].save(commit=False)
            viewC.save()
            args['list'] = ViewEncumbrance.objects.all()
            args['key'] = 'view'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dView(request, id=0):

    ViewEncumbrance.objects.get(id=id).delete()
    args = {}
    args['list'] = ViewEncumbrance.objects.all()
    args['key'] = 'view'
    return render(request, 'view.html', args)

def eView(request, id=0):
    args = {}

    view = ViewEncumbrance.objects.get(id=id)

    if request.POST:
        args['form'] = ViewForm(request.POST)

        if args['form'].is_valid():
            viewT = args['form'].save(commit=False)
            view.Name = viewT.Name
            view.save()
            args['list'] = ViewEncumbrance.objects.all()
            args['key'] = 'view'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = ViewForm(instance = view)
    return render(request, 'add.html', args)

#Type - тип обтяження
def vType(request):
    args = {}
    args['key'] = 'type'
    args['list'] = TypeOfEncumbrance.objects.all()
    return render(request, 'view.html', args)

def aType(request):

    args = {}
    args['form'] = TypeForm

    if request.POST:
        args['form'] = TypeForm(request.POST, request.FILES)
        if args['form'].is_valid():
            typeC = args['form'].save(commit=False)
            typeC.save()
            args['list'] = TypeOfEncumbrance.objects.all()
            args['key'] = 'type'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dType(request, id=0):

    TypeOfEncumbrance.objects.get(id=id).delete()
    args = {}
    args['list'] = TypeOfEncumbrance.objects.all()
    args['key'] = 'type'
    return render(request, 'view.html', args)

def eType(request, id=0):
    args = {}

    type = TypeOfEncumbrance.objects.get(id=id)

    if request.POST:
        args['form'] = TypeForm(request.POST)

        if args['form'].is_valid():
            typeT = args['form'].save(commit=False)
            type.Name = typeT.Name
            type.save()
            args['list'] = TypeOfEncumbrance.objects.all()
            args['key'] = 'type'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = TypeOfEncumbrance(instance = type)
    return render(request, 'add.html', args)

#TypeReg - тип реєстрації
def vTypeReg(request):
    args = {}
    args['key'] = 'typereg'
    args['list'] = TypeReg.objects.all()
    return render(request, 'view.html', args)

def aTypeReg(request):

    args = {}
    args['form'] = TypeRegForm

    if request.POST:
        args['form'] = TypeRegForm(request.POST, request.FILES)
        if args['form'].is_valid():
            typeRC = args['form'].save(commit=False)
            typeRC.save()
            args['list'] = TypeReg.objects.all()
            args['key'] = 'typereg'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dTypeReg(request, id=0):

    TypeReg.objects.get(id=id).delete()
    args = {}
    args['list'] = TypeReg.objects.all()
    args['key'] = 'typereg'
    return render(request, 'view.html', args)

def eTypeReg(request, id=0):
    args = {}

    typeR = TypeReg.objects.get(id=id)

    if request.POST:
        args['form'] = TypeRegForm(request.POST)

        if args['form'].is_valid():
            typeRT = args['form'].save(commit=False)
            typeR.Name = typeRT.Name
            typeR.save()
            args['list'] = TypeReg.objects.all()
            args['key'] = 'typereg'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = TypeRegForm(instance = type)
    return render(request, 'add.html', args)

#Address - адреси проживання осіб
def vAddress(request):
    args = {}
    args['key'] = 'address'
    args['list'] = Address.objects.all()
    return render(request, 'view.html', args)

def aAddress(request):

    args = {}
    args['form'] = AddressForm

    if request.POST:
        args['form'] = AddressForm(request.POST, request.FILES)
        if args['form'].is_valid():
            addrC = args['form'].save(commit=False)
            addrC.save()
            args['list'] = Address.objects.all()
            args['key'] = 'address'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dAddress(request, id=0):

    Address.objects.get(id=id).delete()
    args = {}
    args['list'] = Address.objects.all()
    args['key'] = 'typereg'
    return render(request, 'view.html', args)

def eAddress(request, id=0):
    args = {}

    addrR = Address.objects.get(id=id)

    if request.POST:
        args['form'] = AddressForm(request.POST)

        if args['form'].is_valid():
            addrT = args['form'].save(commit=False)
            addrR.Country = addrT.Country
            addrR.Index = addrT.Index
            addrR.Area = addrT.Area
            addrR.Region = addrT.Region
            addrR.City = addrT.City
            addrR.Street = addrT.Street
            addrR.Home = addrT.Home
            addrR.save()
            args['list'] = Address.objects.all()
            args['key'] = 'address'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = AddressForm(instance = addrR)
    return render(request, 'add.html', args)