from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from users.permissions import IsAdmin, IsAnalystOrAdmin

class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer

    def get_queryset(self):
        queryset = FinancialRecord.objects.all()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [IsAnalystOrAdmin()]
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAnalystOrAdmin
from .services import get_summary

class DashboardSummaryView(APIView):
    permission_classes = [IsAnalystOrAdmin]

    def get(self, request):
        data = get_summary(request.user)
        return Response(data)
from finance.views import DashboardSummaryView