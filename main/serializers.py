from rest_framework import serializers

from main.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FindClosestSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lon = serializers.FloatField()
