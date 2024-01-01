from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class Users(APIView):
    def get(self, request): 
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request): 

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid() : 
            if serializer.data.get('email') != request.data.get('email'):
                return Response(status=status.HTTP_404_NOT_FOUND)
            else: 
                serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)