from rest_framework import serializers
from .models import Goods, Orders


class GoodsSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Goods
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['category']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

# class GoodsByCategorySerializer(serializers.HyperlinkedModelSerializer):
#     user_id = serializers.Field(source='user.id')
#
#     class Meta:
#         model = Group
#         lookup_field = 'user_id'