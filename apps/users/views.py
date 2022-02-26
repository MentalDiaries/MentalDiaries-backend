from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.

class Register(APIView):

    def post(self, request):
        userSerializer = UserSerializer(data=request.data)
        if userSerializer.is_valid():
            userSerializer.save()
            return Response({'Status' : 'Success'}, status=status.HTTP_201_CREATED)
        elif userSerializer.errors['username'][0].code == 'unique':
            return Response({'Status' : 'Failure... User already registered'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            print(userSerializer.errors)
            return Response({'Statuts' : 'Failure... Some error occurred'}, status=status.HTTP_400_BAD_REQUEST)