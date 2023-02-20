from .models import Advocate
from rest_framework import serializers

class AdvocatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['username','bio']

class AdvocatesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['id','username','bio']