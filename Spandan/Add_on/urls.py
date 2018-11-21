from django.urls import path

from . import views

urlpatterns = [
    path('',views.allmatch,name='matches'),
]
