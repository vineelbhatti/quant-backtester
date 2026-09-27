from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from backtests.models import BacktestResult
from backtests.serializers import BacktestResultSerializer

class BacktestResultListView(ListAPIView):
    queryset = BacktestResult.objects.all().order_by("-created_at")
    serializer_class = BacktestResultSerializer