import io

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


import xlsxwriter

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Add_on.models import
from Add_on.serializer import *




class MatchList(APIView):
    def get(self,request):
        try:
            matches = Match.objects.all()
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
            return Response(response)

    def post(self,request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                "status":status.HTTP_201_CREATED,
                "data":{
                "post":serializer.data}
            }
            return Response(response)

    def delete(self,request,match_id):
        match=self.get_object(match_id)
        match.delete()
        response = {"status":"Success","data":"null"}
        return Response(response)


class Search_by_sport(APIView):
    def get(self,request,search):
        try:
            matches = Match.objects.filter(Sport_id==search)
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
            return Response(response)

class Search_by_team(APIView):
    def get(self,request,search):
        try:
            matches = Match.objects.filter(Team1_id==search or Team2_id==search)
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
            return Response(response)

class Search_by_team_and_sport(APIView):
    ef get(self,request,search_team,search_sport):
        try:
            matches = Match.objects.filter(Sport_id==search_sport).filter(Team1_id==search_team or Team2_id==search_team)
            serializer = MatchSerializer(matches,many=True)
            response={
                "status":"Success",
                "data":serializer.data
            }
            return Response(response)
