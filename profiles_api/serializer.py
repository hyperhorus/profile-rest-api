from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializer a name field foe testing out APIView"""
    name = serializers.CharField(max_length=10)