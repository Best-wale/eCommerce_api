
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.prefetch_related('contents')  # Optimize query using related name
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
