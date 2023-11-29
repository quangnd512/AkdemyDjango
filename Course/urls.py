from django.urls import (path,include)
from rest_framework.routers import DefaultRouter
from Course import views

router = DefaultRouter()
router.register('', views.CourseViewSet)

app_name = 'Course'

urlpatterns = [
    path('', include(router.urls)),
]
