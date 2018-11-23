from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler




class MatchDoesNotExist(APIException):
    status_code = 701
    default_detail = 'This request is Not Valid'


class SportDoesNotExist(APIException):
    status_code = 702
    default_detail = 'This sport is Not Valid'


class TeamDoesNotExist(APIException):
    status_code = 703
    default_detail = 'This team is Not Valid'
