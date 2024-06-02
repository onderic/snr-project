from rest_framework import serializers
from .models import PoolSpace

class PoolSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = '__all__'
