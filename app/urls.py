from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Enid Service Docs",
        terms_of_service="",
        contact=openapi.Contact(email="jmedrano9006@gmail.com"),        
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faq/', include('faqs.urls')),
    path('api/devoluciones/', include('returns.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]