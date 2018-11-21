from rest_framework import serializers
from Add_on.models import Match,Sport,Team


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
