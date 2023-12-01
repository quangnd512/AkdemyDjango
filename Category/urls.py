from django.urls import (path,include)
from rest_framework.routers import DefaultRouter
from Category import views

router = DefaultRouter()
router.register('', views.CategoryViewSet)

app_name = 'Category'

urlpatterns = [
    path('', include(router.urls)),
]
