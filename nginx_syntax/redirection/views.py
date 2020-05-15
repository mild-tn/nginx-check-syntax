from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Redirection
from .utils import check_nginx_syntax

from .serializers import RedirectionSerializer

# Create your views here.
class RedirectionListAPI(APIView):
    def get(self, request):
        redirection = Redirection.objects.all()
        serializer = RedirectionSerializer(redirection, many=True)
        result = check_nginx_syntax()
        print(result.returncode)
        print('=====2'*10)
        return  Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = RedirectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
