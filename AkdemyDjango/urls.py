from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),

    path('api/blog/', include('Blog.urls'), name='api-blog'),
    path('api/user/', include('User.urls'), name='api-user'),
    path('api/category/', include('Category.urls'), name='api-category'),
    path('api/course/', include('Course.urls'), name='api-course'),
    
    # path('accounts/', include('allauth.urls')),
]
