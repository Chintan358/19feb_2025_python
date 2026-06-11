from django.urls import *
from myapp.views import *

urlpatterns = [
    path("",index,name="index")
]