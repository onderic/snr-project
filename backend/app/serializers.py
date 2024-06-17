from rest_framework import serializers
from .models import PoolSpace,Tournament, Enrollment

class PoolSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    attendees_count = serializers.SerializerMethodField()
    class Meta:
        model = Tournament
        fields = '__all__'

    def get_attendees_count(self, obj):
        return obj.attendees.count()
    

class EnrollmentReadSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'