from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import CSVParser
from .models import CsvParser
from .serializers import MyModelSerializer

class UploadCSVView(generics.CreateAPIView):
    parser_classes = (CSVParser,)
    serializer_class = MyModelSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        data = file.read().decode('utf-8')
        rows = data.split('\n')
        for row in rows:
            row_data = row.split(',')
            serializer = self.get_serializer(data={
                'field1': row_data[0],
                'field2': row_data[1],
                # add more fields as needed
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)
