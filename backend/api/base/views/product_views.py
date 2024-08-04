from django.shortcuts import render
from rest_framework.response import Response
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from base.models import *
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
