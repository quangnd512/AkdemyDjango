from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [DjangoModelPermissions]

    
