from rest_framework import viewsets
from .serializers import GoodsSerializer
from .models import Goods


class GoodsView(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

