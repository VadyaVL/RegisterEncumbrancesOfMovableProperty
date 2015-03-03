# -*- coding: utf-8 -*-

from serializers import *
from models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Потребує редагування
class PersonList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        person = Person.objects.all()
        #address = Address.objects.all()
        serializer = PersonSerializer(person, many=True, context={'request': request})
        #serializer2 = AddressSerializer(address, many=True, context={'request': request})
        return Response(serializer.data)
        """, serializer2.data"""

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):

    def get_object(selfself, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serialized_dialogue = PersonSerializer(person, context={'request': request})
        return Response(serialized_dialogue.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetail(APIView):

    def get_object(selfself, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serialized_dialogue = AddressSerializer(address, context={'request': request})
        return Response(serialized_dialogue.data)

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TypeOfEncumbranceList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        typeOfEncumbrance = TypeOfEncumbrance.objects.all()
        serializer = TypeOfEncumbranceSerializer(typeOfEncumbrance, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeOfEncumbranceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeOfEncumbranceDetail(APIView):

    def get_object(selfself, pk):
        try:
            return TypeOfEncumbrance.objects.get(pk=pk)
        except TypeOfEncumbrance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        typeOfEncumbrance = self.get_object(pk)
        serialized_dialogue = TypeOfEncumbranceSerializer(typeOfEncumbrance, context={'request': request})
        return Response(serialized_dialogue.data)

    def put(self, request, pk, format=None):
        typeOfEncumbrance = self.get_object(pk)
        serializer = TypeOfEncumbranceSerializer(typeOfEncumbrance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        typeOfEncumbrance = self.get_object(pk)
        typeOfEncumbrance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ViewEncumbranceList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        viewEncumbrance = ViewEncumbrance.objects.all()
        serializer = ViewEncumbranceSerializer(viewEncumbrance, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ViewEncumbranceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewEncumbranceDetail(APIView):

    def get_object(selfself, pk):
        try:
            return ViewEncumbrance.objects.get(pk=pk)
        except ViewEncumbrance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        viewEncumbrance = self.get_object(pk)
        serialized = ViewEncumbranceSerializer(viewEncumbrance, context={'request': request})
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        viewEncumbrance = self.get_object(pk)
        serializer = ViewEncumbranceSerializer(viewEncumbrance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        viewEncumbrance = self.get_object(pk)
        viewEncumbrance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TypeRegList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        typeReg = TypeReg.objects.all()
        serializer = TypeRegSerializer(typeReg, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeRegSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeRegDetail(APIView):

    def get_object(selfself, pk):
        try:
            return TypeReg.objects.get(pk=pk)
        except TypeReg.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        typeReg = self.get_object(pk)
        serialized = TypeRegSerializer(typeReg, context={'request': request})
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        typeReg = self.get_object(pk)
        serializer = TypeRegSerializer(typeReg, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        typeReg = self.get_object(pk)
        typeReg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TypeOfCurrencyList(APIView):

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, format=None):
        typeOfCurrency = TypeOfCurrency.objects.all()
        serializer = TypeOfCurrencySerializer(typeOfCurrency, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypeOfCurrencySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeOfCurrencyDetail(APIView):

    def get_object(selfself, pk):
        try:
            return TypeOfCurrency.objects.get(pk=pk)
        except TypeOfCurrency.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        typeOfCurrency = self.get_object(pk)
        serialized = TypeOfCurrencySerializer(typeOfCurrency, context={'request': request})
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        typeOfCurrency = self.get_object(pk)
        serializer = TypeOfCurrencySerializer(typeOfCurrency, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        typeOfCurrency = self.get_object(pk)
        typeOfCurrency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)