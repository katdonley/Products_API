from rest_framework.decorators import api_view
from rest_framework.response import Response

import products
from .serializers import ProductSerializer
from .models import Product
from products import serializers

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)