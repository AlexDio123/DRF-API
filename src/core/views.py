from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data={
            'name':'Alex',
            'age':20
        }
        return Response(data)