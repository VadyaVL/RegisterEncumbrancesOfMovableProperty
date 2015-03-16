# -*- coding: utf-8 -*-
from models import *
from rest_framework import serializers

class AddressSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Country = validated_data.get('Country', instance.Country)
        instance.Index = validated_data.get('Index', instance.Index)
        instance.Region = validated_data.get('Region', instance.Region)
        instance.Area = validated_data.get('Area', instance.Area)
        instance.City = validated_data.get('City', instance.City)
        instance.Street = validated_data.get('Street', instance.Street)
        instance.Home = validated_data.get('Home', instance.Home)

        instance.save()

        return instance

    class Meta:
        model = Address
        fields = (
            #'url',
            'id',
            'Country',
            'Index',
            'Region',
            'Area',
            'City',
            'Street',
            'Home',
        )

class PersonSerializer(serializers.HyperlinkedModelSerializer):

    Address = AddressSerializer(read_only=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Identification = validated_data.get('Identification', instance.Identification)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.NonResidentForeigner = validated_data.get('NonResidentForeigner', instance.NonResidentForeigner)
        instance.MoreInformation = validated_data.get('MoreInformation', instance.MoreInformation)
        instance.save()

        return instance

    class Meta:
        model = Person
        fields = (
            #'url',
            'id',
            'Identification',
            'Name',
            'NonResidentForeigner',
            'MoreInformation',
            'Address',
        )

class TypeOfEncumbranceSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return TypeOfEncumbrance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

    class Meta:
        model = TypeOfEncumbrance
        fields = (
            'id',
            'Name',
        )

class ViewEncumbranceSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return ViewEncumbrance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

    class Meta:
        model = ViewEncumbrance
        fields = (
            'id',
            'Name',
        )

class TypeRegSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return TypeReg.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

    class Meta:
        model = TypeReg
        fields = (
            'id',
            'Name',
        )

class TypeOfCurrencySerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return TypeOfCurrency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

    class Meta:
        model = TypeOfCurrency
        fields = (
            'id',
            'Name',
        )

class EncumbranceSerializer(serializers.HyperlinkedModelSerializer):
    TypeOfEncumbrance = serializers.StringRelatedField(read_only=True)
    TypeReg = serializers.StringRelatedField(read_only=True)
    ViewEncumbrance = serializers.StringRelatedField(read_only=True)
    #TypeOfEncumbrance = TypeOfEncumbranceSerializer(required=False)
    #TypeReg = TypeRegSerializer(required=False)
    #ViewEncumbrance = ViewEncumbranceSerializer(required=False)


    def create(self, validated_data):
        return Encumbrance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.NStatement = validated_data.get('NStatement', instance.NStatement)
        instance.DateStatement = validated_data.get('DateStatement', instance.DateStatement)
        instance.TypeOfEncumbrance = validated_data.get('TypeOfEncumbrance', instance.TypeOfEncumbrance)
        instance.TypeReg = validated_data.get('TypeReg', instance.TypeReg)
        instance.ViewEncumbrance = validated_data.get('ViewEncumbrance', instance.ViewEncumbrance)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.AddedInfo = validated_data.get('AddedInfo', instance.AddedInfo)
        instance.save()
        return instance

    class Meta:
        model = Encumbrance
        fields = (
            'id',
            'NStatement',
            'DateStatement',
            'TypeOfEncumbrance',
            'TypeReg',
            'ViewEncumbrance',
            'Date',
            'AddedInfo',
        )

class TermsSerializer(serializers.HyperlinkedModelSerializer):
    TypeOfCurrency = serializers.StringRelatedField(read_only=True)
    Encumbrance = serializers.StringRelatedField(read_only=True)
    def create(self, validated_data):
        return Terms.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.SizeObligations = validated_data.get('SizeObligations', instance.SizeObligations)
        instance.LimitDate = validated_data.get('LimitDate', instance.LimitDate)
        instance.AddedInfo = validated_data.get('AddedInfo', instance.AddedInfo)
        instance.TypeOfCurrency = validated_data.get('TypeOfCurrency', instance.TypeOfCurrency)
        instance.Encumbrance = validated_data.get('Encumbrance', instance.Encumbrance)
        instance.save()
        return instance

    class Meta:
        model = Terms
        fields = (
            'id',
            'SizeObligations',
            'LimitDate',
            'AddedInfo',
            'TypeOfCurrency',
            'Encumbrance'
        )

class ObjectSerializer(serializers.HyperlinkedModelSerializer):

    Encumbrance = EncumbranceSerializer(read_only=True)

    def create(self, validated_data):
        return Object.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.SerialNumber = validated_data.get('SerialNumber', instance.SerialNumber)
        instance.RegNumber = validated_data.get('RegNumber', instance.RegNumber)
        instance.AddedInfoForUNMovable = validated_data.get('AddedInfoForUNMovable', instance.AddedInfoForUNMovable)
        instance.Encumbrance = validated_data.get('Encumbrance', instance.Encumbrance)
        instance.save()

        return instance

    class Meta:
        model = Object
        fields = (
            #'url',
            'id',
            'Name',
            'SerialNumber',
            'RegNumber',
            'AddedInfoForUNMovable',
            'Encumbrance',
        )


class DocumentBaseSerializer(serializers.HyperlinkedModelSerializer):

    Encumbrance = EncumbranceSerializer(read_only=True)

    def create(self, validated_data):
        return Object.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Number = validated_data.get('Number', instance.Number)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.PublisherName = validated_data.get('PublisherName', instance.PublisherName)
        instance.Encumbrance = validated_data.get('Encumbrance', instance.Encumbrance)
        instance.save()

        return instance

    class Meta:
        model = DocumentBase
        fields = (
            #'url',
            'id',
            'Name',
            'Number',
            'Date',
            'PublisherName',
            'Encumbrance',
        )