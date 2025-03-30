from django.urls import path,include
from .views import CategoryListAPIView

urlpatterns = [
    

    path('api-auth/', include('rest_framework.urls')),
    path('data/',CategoryListAPIView.as_view(),name='api')
]