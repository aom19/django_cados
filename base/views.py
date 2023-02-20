from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models  import Q

from .models import Advocate
from .serializers import AdvocatesListSerializer, AdvocatesDetailSerializer


@api_view(['GET'])
def endpoints(request):
    data = [
        '/advocates',
        '/advocates/<id>',

    ]
    return Response(data)


@api_view(['GET', "POST"])
def advocates_list(request):
    # handle GET REQUEST
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocatesListSerializer(advocates, many=True)
        return Response(serializer.data)
    # handle POST REQUEST
    elif request.method == 'POST':
        serializer = AdvocatesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', "PUT", "DELETE"])
def advocates_detail(request,id):
    # handle GET REQUEST
    if request.method == 'GET':
        advocate = Advocate.objects.get(id=id)

        serializer = AdvocatesDetailSerializer(advocate, many=False)
        return Response(serializer.data)
    # handle PUT REQUEST
    elif request.method == 'PUT':
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocatesDetailSerializer(instance=advocate, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    # handle DELETE REQUEST
    elif request.method == 'DELETE':
        advocate = Advocate.objects.get(id=id)
        advocate.delete()
        return Response('Item successfully deleted!')





