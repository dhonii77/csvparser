from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyTable
from .serializers import MyTableSerializer

class Top50View(APIView):
    def get(self, request):
        column_name = request.query_params.get('column_name')
        sort_order = request.query_params.get('sort_order')

        if column_name and sort_order:
            if sort_order.lower() == 'asc':
                order_by = column_name
            elif sort_order.lower() == 'desc':
                order_by = f'-{column_name}'
            else:
                return Response({'error': 'Invalid sort order. Must be "asc" or "desc".'}, status=400)

            queryset = MyTable.objects.all().order_by(order_by)[:50]
            serializer = MyTableSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Missing query parameters. Must include "column_name" and "sort_order".'}, status=400)
