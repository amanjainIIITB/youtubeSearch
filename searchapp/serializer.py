from rest_framework import serializers
from .models import ContentDetails

class ContentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDetails
        fields = '__all__'