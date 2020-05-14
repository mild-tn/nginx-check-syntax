from rest_framework import serializers

from .models import Redirection

class RedirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirection
        fields = "__all__"