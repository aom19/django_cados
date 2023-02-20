from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
advocates = [
    {
        'id':1,
        'name':'Dennis',
    },
    {
        'id':2,
        'name':'Dennis2',
    }
]


@api_view(['GET'])
def endpoints(request):
    data = [
        '/advocates',
        '/advocates/<id>',

    ]
    return Response(data)


@api_view(['GET'])
def advocates_list(request):

    return Response(advocates)


@api_view(['GET'])
def advocates_detail(request,id):
    advocate = next(item for item in advocates if item["id"] == id)
    return Response(advocate)


def add_advocate(request):
    advocate = {
        'id':3,
        'name':'Dennis3',
    }
    advocates.append(advocate)
    return JsonResponse(advocates)


def index(request):
    return JsonResponse("Hello, world. You're at the polls index.")



