from rest_framework import serializers

from core.models import Reporting

class ReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporting
        fields = '__all__'