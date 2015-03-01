# -*- coding: utf-8 -*-
from django.db import models

# Категорії
class ViewEncumbrance(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Вид')

    def __str__(self):
        return  self.Name.encode('utf8')

    class Meta:
        db_table = 'ViewEncumbrance'

class TypeOfEncumbrance(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Тип')

    def __str__(self):
        return  self.Name.encode('utf8')

    class Meta:
        db_table = 'TypeOfEncumbrance'

class TypeReg(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Тип реєстрації')

    def __str__(self):
        return  self.Name.encode('utf8')

    class Meta:
        db_table = 'TypeReg'

class TypeOfCurrency(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Валюта')

    def __str__(self):
        return  self.Name.encode('utf8')

    class Meta:
        db_table = 'TypeOfCurrency'

# Сутності які додаємо окремо
class Person(models.Model):
    Identification = models.CharField(max_length=10, db_column='Identification', null=False, verbose_name='Ідентифікаційний номер')
    NonResidentForeigner = models.BooleanField(db_column='NonResidentForeigner', default=False, verbose_name='Не резидент')
    Name = models.CharField(max_length=100, db_column='Name', null=False, verbose_name='Ф.І.О.')
    MoreInformation = models.CharField(max_length=500, db_column='MoreInformation', null=True, verbose_name='Дод. інф.')
    Address = models.ForeignKey('Address')

    def __str__(self):
        return (self.Name + ' (' + self.Identification + ')').encode('utf8')

    class Meta:
        db_table = 'Person'

class Address(models.Model):
    Country = models.CharField(max_length=45, db_column='Country', default='Ukraine', null=False, verbose_name='Країна')
    Index = models.CharField(max_length=45, db_column='Index', null=False, verbose_name='Індекс')
    Region = models.CharField(max_length=45, db_column='Region', null=False, verbose_name='Область')
    Area = models.CharField(max_length=45, db_column='Area', null=True, verbose_name='Район')
    City = models.CharField(max_length=45, db_column='City', null=False, verbose_name='Місто/н.п.')
    Street = models.CharField(max_length=45, db_column='Street', null=False, verbose_name='Вулиця')
    Home = models.CharField(max_length=45, db_column='Home', null=False, verbose_name='дім/буд.')

    def __str__(self):
        return (self.Country + ', ' + self.Region + ', ' + self.Area + ', ' + self.City).encode('utf8')

    class Meta:
        db_table = "Address"

# На одній сторінці заповнюємо інформацію про
class Encumbrance(models.Model):
    NStatement = models.IntegerField(db_column='NStatement', null=False, verbose_name='Номер заяви')
    DateStatement = models.DateField(db_column='DateStatement', null=False, verbose_name='Дата заяви')
    TypeOfEncumbrance = models.ForeignKey(TypeOfEncumbrance)
    TypeReg = models.ForeignKey(TypeReg)
    ViewEncumbrance = models.ForeignKey(ViewEncumbrance)
    Date = models.DateField(db_column='Date', null=False, verbose_name='Дата')
    AddedInfo = models.CharField(max_length=500, db_column='AddedInfo', null=True, verbose_name='Дод. інф.')
    #Обтяжувач
    WPerson = models.ManyToManyField(Person, related_name='W', help_text='Виберіть декілька обтяжувачів')
    #Не обтяжувач
    SPerson = models.ManyToManyField(Person, related_name='S', help_text='Виберіть декілька боржників')

    class Meta:
        db_table = 'Encumbrance'

class Object(models.Model):
    Name = models.CharField(max_length=45, db_column='Name', null=False, verbose_name='Назва')
    SerialNumber = models.CharField(max_length=45, db_column='SerialNumber', null=False, verbose_name='Серійний номер')
    RegNumber = models.CharField(max_length=45, db_column='RegNumber', null=False, verbose_name='Номер реєстрації')
    AddedInfoForUNMovable = models.CharField(max_length=500, db_column='AddedInfoForUNMovable', null=False, verbose_name='Дод. інф.(нерухоме)')
    Encumbrance = models.OneToOneField(Encumbrance)

    class Meta:
        db_table = 'Object'

class DocumentBase(models.Model):
    Name = models.CharField(max_length=45, db_column='Name', null=False, verbose_name='Назва')
    Number = models.CharField(max_length=45, db_column='Number', null=False, verbose_name='Номер')
    Date = models.DateField(db_column='Date', null=False, verbose_name='Дата')
    PublisherName = models.CharField(max_length=100, db_column='PublisherName', null=False, verbose_name='Публікатор')
    Encumbrance = models.OneToOneField(Encumbrance)

    class Meta:
        db_table = 'DocumentBase'

class Terms(models.Model):
    SizeObligations = models.IntegerField(null=False, db_column='SizeObligations', verbose_name='Розмір облігації')
    LimitDate = models.DateField(db_column='LimitDate', verbose_name='Строк')
    AddedInfo = models.CharField(max_length=500, db_column='AddedInfo', null=False, verbose_name='Дод. інф.')
    TypeOfCurrency = models.ForeignKey(TypeOfCurrency)
    Encumbrance = models.OneToOneField(Encumbrance)

    class Meta:
        db_table = 'Terms'
