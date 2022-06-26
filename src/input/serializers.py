from .models import FormData
from rest_framework import serializers


class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = "__all__"
