from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
def Register_user(request):
    # if request.method=='post':
    #     serializer=AuthSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #     user=User.objects.get(username=request.data['username'])
    #     token=Token.objects.get(user=user) #to generate token
    #     print(token)
    #     return Response({'user':serializer.data,'token':token.key})
    # return Response('Registration Successfull')
    if request.method=="POST":
        serializer1=User_detailSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        user = User.objects.get(username=request.data['username'])  #fetching user details
        token = Token.objects.get(user=user) #fetching the token
        serializer =AuthSerializer(user)  #to convert data to return

        return Response({'user': serializer.data, 'token': token.key},status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def Login_user(request):
    if request.method=='POST':
        x=authenticate(username=request.data['username'],password=request.data['password'])
        if x is not None:
            user = User.objects.get(username=request.data['username'])
            serializer = AuthSerializer(user)
            token,new = Token.objects.get_or_create(user=user)
            return Response({"user_details":serializer.data,"token":token.key},status=status.HTTP_200_OK)
        else:
            return Response('Bad Request',status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def Logout_user(request):
    request.user.auth_token.delete()
    return Response("logout successfull")




