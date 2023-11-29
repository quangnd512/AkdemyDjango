from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Category
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [DjangoModelPermissions]

    
