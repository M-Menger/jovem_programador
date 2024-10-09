from rest_framework import serializers
from api import models

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Market
        fields = '__all__'