from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ReportingSerializer
from core.models import Reporting


"""
Below Function going to display all the reportings stored in the data base.
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reportingList(request):
    reportings = Reporting.objects.all()
    serializer = ReportingSerializer(reportings, many = True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reportingDetail(request, pk):
    reportings = Reporting.objects.get(id=pk)
    serializer = ReportingSerializer(reportings, many = False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reportingUpdate(request, pk):
    reportings = Reporting.objects.get(id = pk)
    serializer = ReportingSerializer(instance=reportings, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reportingCreate(request):
    serializer = ReportingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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