from rest_framework import serializers
from .models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'flavor', 'created_at', 'updated_at')
        model = Fruit