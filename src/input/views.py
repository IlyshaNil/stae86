from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import FormData
from .serializers import FormDataSerializer


def main(request):
    return render(request, "main.html")


class FormDataAPICreate(CreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer


class FormDataAPIList(ListAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer
