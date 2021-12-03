from rest_framework import serializers

from .models import *

class HotelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = '__all__'