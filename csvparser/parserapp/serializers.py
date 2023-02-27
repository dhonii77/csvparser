from rest_framework import serializers
from .models import CsvParser

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvParser
        fields = '__all__'
