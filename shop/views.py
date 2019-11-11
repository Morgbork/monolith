from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import GoodsSerializer, CategoriesSerializer, OrdersSerializer
from .models import Goods, Orders


class GoodsView(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get_queryset(self):
        # if self.request.cat:
        queryset = Goods.objects.all()
        category = self.request.query_params.get('cat', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
        # return Goods.objects.filter(category=self.request.cat)


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Goods.objects.raw('SELECT id, category FROM shop_goods GROUP BY category')


class OrdersView(APIView):
    serializer_class = OrdersSerializer

    def get(self, request):
        order = get_object_or_404(Orders, id=request.order_number)
        return Response({"order": order})


class GoodsByCategoryView(generics.ListAPIView):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        cat = self.kwargs['cat']
        return Goods.objects.filter(category=cat)
