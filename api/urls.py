from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('reporting-list/', views.reportingList, name="reporting-list"),
  ]