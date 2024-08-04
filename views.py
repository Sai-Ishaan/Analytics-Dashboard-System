from django.http import JsonResponse
from django.shortcuts import render
from dash.models import Order
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard.html', {})

def pivot_data(request):
        dataset = Order.objects.all()
        data = serializers.serialize('json', dataset)
        return JsonResponse(data, safe=False)