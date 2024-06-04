from rest_framework import serializers
from .models import PoolSpace,Tournament

class PoolSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'
