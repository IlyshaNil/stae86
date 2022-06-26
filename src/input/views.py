from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FormData
from .serializers import FormDataSerializer


def main(request):
    return render(request, "main.html")


class FormDataViewSet(ModelViewSet):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer
    