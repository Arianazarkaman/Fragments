from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import AbstractUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication



class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
       
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "User created successfully!",  "token": token.key}, status=status.HTTP_201_CREATED)
       
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny] 
    
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        serializer = LoginSerializer(data={"username": username, "password": password})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)    
            return Response({"message": "You are now Logged in!",  "token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"})
    

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)


class Dashboard(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "user": user.username,  
            "message": "Welcome to your story land"
        })

class pci(APIView):
    def post():
        
        return Response("hello")