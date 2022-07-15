from django.urls import path
from survey.views import *
urlpatterns = [
    path('',survey_view , name='survy')
]