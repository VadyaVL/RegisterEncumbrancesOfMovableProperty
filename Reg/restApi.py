from serializers import *
from models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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