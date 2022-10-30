from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('reporting-list/', views.reportingList, name="reporting-list"),
    path('reporting-detail/<str:pk>/', views.reportingDetail, name="reporting-Detail"),
    path('reporting-update/<str:pk>/', views.reportingUpdate, name="reporting-update"),
    path('reporting-create/', views.reportingCreate, name="reporting-Create"),
  ]