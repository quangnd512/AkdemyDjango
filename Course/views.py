from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Course
from .serializers import CourseSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Course'])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [DjangoModelPermissions]

    
