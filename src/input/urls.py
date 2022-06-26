from django.urls import path
from .views import FormDataViewSet, main


urlpatterns = [
    path("", main, name="main"),
    path("api/v1/create/", FormDataViewSet.as_view({'post': 'create'})),
    path("api/v1/list/", FormDataViewSet.as_view({'get': 'list'})),
]
