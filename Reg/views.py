# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
from forms import *
import datetime

from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def add(request):

    args = {}
    args['formE'] = EncumbranceForm
    args['formO'] = ObjectForm
    args['formD'] = DocumentForm
    args['formT'] = TermForm

    if request.POST:
        args['formE'] = EncumbranceForm(request.POST, request.FILES)
        args['formO'] = ObjectForm(request.POST, request.FILES)
        args['formD'] = DocumentForm(request.POST, request.FILES)
        args['formT'] = TermForm(request.POST, request.FILES)

        if args['formE'].is_valid() and args['formO'] and args['formD'] and args['formT']:
            emer = args['formE'].save(commit=False)
            emer.Date = datetime.date.today()
            emer.save()

            for i in request.POST.getlist('SPerson'):
                emer.SPerson.add(Person.objects.get(id=i))
            for i in request.POST.getlist('WPerson'):
                emer.WPerson.add(Person.objects.get(id=i))
            emer.save()

            ob = args['formO'].save(commit=False)
            ob.Encumbrance = emer
            ob.save()

            doc = args['formD'].save(commit=False)
            doc.Encumbrance = emer
            doc.save()

            term = args['formT'].save(commit=False)
            term.Encumbrance = emer
            term.save()

            args['list'] = Encumbrance.objects.all()
            args['key'] = 'encumbrance'
            return render(request, 'view.html', args)

    return render(request, 'addHead.html', args)

def view(request):
    args = {}
    args['key'] = 'encumbrance'
    args['list'] = Encumbrance.objects.all()
    return render(request, 'view.html', args)

def delete(request, id=0):
    enc = Encumbrance.objects.get(id=id)
    try:
        Object.objects.get(Encumbrance=enc).delete()
    except:
        pass
    try:
        DocumentBase.objects.get(Encumbrance=enc).delete()
    except:
        pass
    try:
        Terms.objects.get(Encumbrance=enc).delete()
    except:
        pass

    enc.WPerson.clear()
    enc.SPerson.clear()
    enc.delete()

    args = {}
    args['key'] = 'encumbrance'
    args['list'] = Encumbrance.objects.all()
    return render(request, 'view.html', args)

def edit(request, id=0):
    args = {}

    enc = Encumbrance.objects.get(id=id)
    term = Terms.objects.get(Encumbrance=enc)
    doc = DocumentBase.objects.get(Encumbrance=enc)
    obj = Object.objects.get(Encumbrance=enc)

    if request.POST:
        args['formE'] = EncumbranceForm(request.POST)
        args['formT'] = TermForm(request.POST)
        args['formD'] = DocumentForm(request.POST)
        args['formO'] = ObjectForm(request.POST)
        if args['formE'].is_valid() and args['formT'].is_valid() and args['formD'].is_valid() and args['formO'].is_valid():

            termT = args['formT'].save(commit=False)
            term.SizeObligations = termT.SizeObligations
            term.LimitDate = termT.LimitDate
            term.AddedInfo = termT.AddedInfo
            term.TypeOfCurrency = termT.TypeOfCurrency
            term.save()

            docT = args['formD'].save(commit=False)
            doc.Name = docT.Name
            doc.Number = docT.Number
            doc.Date = docT.Date
            doc.PublisherName = docT.PublisherName
            doc.save()

            objT = args['formO'].save(commit=False)
            obj.Name = objT.Name
            obj.SerialNumber = objT.SerialNumber
            obj.RegNumber = objT.RegNumber
            obj.AddedInfoForUNMovable = objT.AddedInfoForUNMovable
            obj.save()

            encT = args['formE'].save(commit=False)
            enc.NStatement = encT.NStatement
            enc.DateStatement = encT.DateStatement
            enc.TypeOfEncumbrance = encT.TypeOfEncumbrance
            enc.TypeReg = encT.TypeReg
            enc.ViewEncumbrance = encT.ViewEncumbrance
            enc.TypeOfEncumbrance = encT.TypeOfEncumbrance
            enc.AddedInfo = encT.AddedInfo
            enc.TypeOfEncumbrance = encT.TypeOfEncumbrance

            enc.WPerson.clear()
            enc.SPerson.clear()

            for i in request.POST.getlist('SPerson'):
                enc.SPerson.add(Person.objects.get(id=i))
            for i in request.POST.getlist('WPerson'):
                enc.WPerson.add(Person.objects.get(id=i))
            enc.save()

            args['list'] = Encumbrance.objects.all()
            args['key'] = 'encumbrance'
            return render(request, 'view.html', args)
        else:
            return render(request, 'addHead.html', args)
    args['formE'] = EncumbranceForm(instance = enc)
    args['formD'] = DocumentForm(instance = doc)
    args['formT'] = TermForm(instance = term)
    args['formO'] = ObjectForm(instance = obj)
    return render(request, 'addHead.html', args)

#додати редагування обтяження і готово

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

#Person - особи
def vPerson(request):
    args = {}
    args['key'] = 'person'
    args['list'] = Person.objects.all()
    return render(request, 'view.html', args)

def aPerson(request):

    args = {}
    args['form'] = PersonForm

    if request.POST:
        args['form'] = PersonForm(request.POST, request.FILES)
        if args['form'].is_valid():
            perC = args['form'].save(commit=False)
            perC.save()
            args['list'] = Person.objects.all()
            args['key'] = 'person'
            return render(request, 'view.html', args)

    return render(request, 'add.html', args)

def dPerson(request, id=0):

    Person.objects.get(id=id).delete()
    args = {}
    args['list'] = Person.objects.all()
    args['key'] = 'person'
    return render(request, 'view.html', args)

def ePerson(request, id=0):
    args = {}

    perR = Person.objects.get(id=id)

    if request.POST:
        args['form'] = PersonForm(request.POST)

        if args['form'].is_valid():
            perT = args['form'].save(commit=False)
            perR.Identification = perT.Identification
            perR.Name = perT.Name
            perR.NonResidentForeigner = perT.NonResidentForeigner
            perR.MoreInformation = perT.MoreInformation
            perR.Address = perT.Address
            perR.save()
            args['list'] = Person.objects.all()
            args['key'] = 'person'
            return render(request, 'view.html', args)
        else:
            return render(request, 'add.html', args)
    args['form'] = PersonForm(instance = perR)
    return render(request, 'add.html', args)