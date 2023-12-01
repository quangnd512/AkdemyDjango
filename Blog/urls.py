from django.urls import (path,include)
from rest_framework.routers import DefaultRouter
from Blog import views

router = DefaultRouter()
router.register('', views.BlogViewSet)

app_name = 'Blog'

urlpatterns = [
    path('', include(router.urls)),
]
