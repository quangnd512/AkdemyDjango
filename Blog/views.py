from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Blog'])
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


    
