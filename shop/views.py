from rest_framework import viewsets
from .serializers import GoodsSerializer, CategoriesSerializer
from .models import Goods


class GoodsView(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Goods.objects.raw('SELECT id, category FROM shop_goods GROUP BY category')
