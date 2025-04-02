import django_filters
from .models import Product


"""  Filter products  """
class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__category_name',lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category']
    
class ProductSearch(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='name',lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['search']