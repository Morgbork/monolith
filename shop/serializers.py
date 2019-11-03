from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Goods
        fields = '__all__'
