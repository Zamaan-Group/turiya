from rest_framework import generics, views, response
from .models import Product, Category
from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer
from django.db.models import Q


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        cat = self.request.query_params.get('cat')
        brand = self.request.query_params.get('brand')
        color = self.request.query_params.get('color')
        if cat:
            qs = self.queryset.filter(category=cat)
        if brand:
            qs = self.queryset.filter(Q(category=cat), Q(brand=brand))
        if color:
            qs = self.queryset.filter(Q(category=cat), Q(brand=brand), Q(color=color))
        return qs


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductFilterAPI(views.APIView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        data = dict()
        data['brands'] = [self.queryset.order_by('brand').distinct('brand').first()]
        data['colors'] = self.queryset.order_by('color').distinct('color').first()
        data['made_ins'] = self.queryset.order_by('made_in').distinct('made_in').first()
        print(data)
        return response.Response(data)
