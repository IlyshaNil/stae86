from django.shortcuts import render
from rest_framework import generics
from .models import FormData
from .serializers import FormDataSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

def main(request):
    return render(request, 'main.html')


def input_list(request):
    pass


class FormDataAPICreate(generics.ListCreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        data = generics.ListCreateAPIView.get(self, request, *args, **kwargs).data
        return Response({'data': data})


class FormDataAPIUpdate(generics.UpdateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer