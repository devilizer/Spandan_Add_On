import io

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Add_on.models import Team,Sport,Match
from Add_on.serializers import MatchSerializer,SportSerializer,TeamSerializer
from Add_on.exception import MatchDoesNotExist,SportDoesNotExist,TeamDoesNotExist




class MatchList(APIView):
    def get(self,request):
        try:
            matches = Match.objects.all()
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
        except ObjectDoesNotExist:
            raise MatchDoesNotExist
        return Response(response)
    def post(self,request):
        #import ipdb; ipdb.set_trace()

        try:
            change=request.data
            serializer = MatchSerializer(data=change[0])
            if serializer.is_valid():
                serializer.save()
                response={
                    "status":status.HTTP_201_CREATED,
                    "data":{
                    "post":serializer.data}
                    }
        except ObjectDoesNotExist:
            raise MatchDoesNotExist
        return Response(response)

    def delete(self,request,match_id):
        match=self.get_object(match_id)
        match.delete()
        response = {"status":"Success","data":"null"}
        return Response(response)


class Search_by_sport(APIView):
    def get(self,request,sport):
        try:
            matches = Match.objects.filter(Sport_id=sport)
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
        except ObjectDoesNotExist:
            raise MatchDoesNotExist
        return Response(response)


class Search_by_team(APIView):
    def get(self,request,team):
        try:
            matches_team1 = Match.objects.filter(Team1_id=team)
            matches_team2 = Match.objects.filter(Team2_id=team)
            matches = matches_team1|matches_team2
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
        except ObjectDoesNotExist:
            raise MatchDoesNotExist
        return Response(response)


class Search_by_team_and_sport(APIView):
    def get(self,request,team,sport):
        try:
            matches_team1 = Match.objects.filter(Sport_id=sport).filter(Team1_id=team)
            matches_team2 = Match.objects.filter(Sport_id=sport).filter(Team2_id=team)
            matches = matches_team1|matches_team2
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
        except ObjectDoesNotExist:
            raise MatchDoesNotExist
        return Response(response)


class SportList(APIView):
    def get(self,request):
        try:
            sports=Sport.objects.all()
            serializer=SportSerializer(sports,many=True)
            response={
                "status":"Success",
                "data" : serializer.data
            }
        except ObjectDoesNotExist:
            raise SportDoesNotExist
        return Response(response)


class TeamList(APIView):
    def get(self,request):
        try:
            teams=Team.objects.all()
            team_serializer=TeamSerializer(teams,many=True)
            response={
                "status":"Success",
                "data":team_serializer.data
            }
        except ObjectDoesNotExist:
            raise TeamDoesNotExist
        return Response(response)

class TeamListExcept(APIView):
    def get(self,request,team):
        try:
            teams=Team.objects.exclude(id=team)
            team_serializer=TeamSerializer(teams,many=True)
            response={
                "status":"Success",
                "data":team_serializer.data
            }
        except ObjectDoesNotExist:
            raise TeamDoesNotExist
        return Response(response)
