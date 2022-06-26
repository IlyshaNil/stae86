from django.db import router
from django.urls import path, include
from .views import *


urlpatterns = [
    path("", main, name="main"),
    path("api/v1/create/", FormDataAPICreate.as_view()),
    path("api/v1/list/", FormDataAPIList.as_view(), name="list"),
]
