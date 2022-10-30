from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReportingSerializer
from core.models import Reporting
"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/reporting-list/',
        'Detail View' : '/reporting-detail/<str:pk>/',
        'Create' : '/reporting-create/',
        'Update' : '/reporting-update/<str:pk>/',
        #'Delete' : '/reporting-delete/<str:pk>/',
    }
    return Response(api_urls)