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