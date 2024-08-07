from rest_framework import serializers

from accounts.models import User
from .models import MpesaTransaction, PoolSpace, Tournament, Enrollment

class PoolSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = '__all__'

class PoolSpaceCo(serializers.ModelSerializer):
    class Meta:
        model = PoolSpace
        fields = ('latitude', 'longitude')

class TournamentSerializer(serializers.ModelSerializer):
    pool_space = serializers.PrimaryKeyRelatedField(queryset=PoolSpace.objects.all())
    organizer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
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

class MpesaTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaTransaction
        fields = '__all__' 
