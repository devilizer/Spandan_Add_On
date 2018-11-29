from django.urls import path , re_path
from django.conf.urls import url
from . import views
from Add_on.views import *
from Add_on.api import *

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^matches/$',MatchList.as_view()),
    url(r'^team/(?P<team>[0-9]+)/$',Search_by_team.as_view()),
    url(r'^sport/(?P<sport>[0-9]+)/$',Search_by_sport.as_view()),
    url(r'^team_sport/(?P<team>[0-9]+)/(?P<sport>[0-9]+)/$',Search_by_team_and_sport.as_view()),
    url(r'^teams/$',TeamList.as_view()),
    url(r'^sports/$',SportList.as_view()),
    url(r'^team_except/(?P<team>[0-9]+)/$',TeamListExcept.as_view()),
]
