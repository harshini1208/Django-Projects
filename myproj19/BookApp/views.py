from django.shortcuts import render
from.models import Book
from.serializers import Bookserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(['GET','POST'])
def Book_data(request):
    if request.method=='GET':
        book=Book.objects.all()
        serializer=Bookserializers(book,many=True)
        return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
    if request.method=='POST':
        serializer=Bookserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def Book_details(request,id):
    try:
        book=Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Bookserializers(book)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=Bookserializers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


