from rest_framework import serializers
from .models import PoolSpace,Tournament, Enrollment

class PoolSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'