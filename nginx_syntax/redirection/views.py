from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Redirection

from .serializers import RedirectionSerializer

# Create your views here.
class RedirectionListAPI(APIView):
    def get(self, request):
        redirection = Redirection.objects.all()
        serializer = RedirectionSerializer(redirection, many=True)

        return  Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = RedirectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
