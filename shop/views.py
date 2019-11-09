from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import GoodsSerializer, CategoriesSerializer, OrdersSerializer
from .models import Goods, Orders


class GoodsView(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Goods.objects.raw('SELECT id, category FROM shop_goods GROUP BY category')


class OrdersView(APIView):
    serializer_class = OrdersSerializer

    def get(self, request):
        order = get_object_or_404(Orders, id=request.order_number)
        return Response({"order": order})
