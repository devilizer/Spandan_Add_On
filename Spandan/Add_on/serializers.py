from rest_framework import serializers
from Add_on.models import Match,Sport,Team


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
