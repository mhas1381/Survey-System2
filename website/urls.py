from django.urls import URLPattern, path
from website.views import *
app_name = 'website'

urlpatterns=[
    path('' , index_view , name="index")

]