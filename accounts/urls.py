from django.urls import path
from accounts.views import *
app_name='accounts'

urlpatterns = [
    path('login' , login_page , name ='login'),
    path('survey',logged_in,name='survey')
]