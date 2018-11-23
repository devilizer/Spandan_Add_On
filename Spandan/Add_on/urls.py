from django.urls import path
from django.conf.urls import url
from . import views
from Add_on.api import *
urlpatterns = [

    url('',views.allmatch,name='matches'),
    url('matches/',MatchList.as_view()),
    url('team/<int:team>/',Search_by_team.as_view()),
    url('sport/<int:sport>/',Search_by_sport.as_view()),
    url('team_sport/<int:team>/<int:sport>/',Search_by_team_and_sport.as_view()),
    url('teams/',TeamList.as_view()),
    url('sports/',SporrtList.as_view()),

]
