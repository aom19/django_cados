from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models  import Q
from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Advocate, Company
from .serializers import AdvocatesListSerializer, AdvocatesDetailSerializer , CompanyListSerializer


@api_view(['GET'])
def endpoints(request):
    data = [
        '/advocates',
        '/advocates/<id>',

    ]
    return Response(data)



class AdvocatesList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get (self,request):
        advocates = Advocate.objects.all()
        serializer = AdvocatesListSerializer(advocates,many=True)
        return Response(serializer.data)

    def post (self,request):
        serializer = AdvocatesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class AdvocateDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self,id):
        try:
            return Advocate.objects.get(id=id)
        except Advocate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id,format=None):
        advocate = self.get_object(id)
        serializer = AdvocatesDetailSerializer(advocate)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        advocate = self.get_object(id)
        serializer = AdvocatesDetailSerializer(advocate,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        advocate = self.get_object(id)
        advocate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,format=None):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CompanyListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


