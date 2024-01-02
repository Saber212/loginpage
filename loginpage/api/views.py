from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserModel
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Users(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request): 
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request): 

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid() : 
          
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)