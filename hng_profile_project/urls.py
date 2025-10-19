# hng_profile_project/urls.py

from django.contrib import admin
from django.urls import path, include

# drf-yasg imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# This sets up the metadata for your API documentation
schema_view = get_schema_view(
   openapi.Info(
      title="HNG Stage 0 Profile API",
      default_version='v1',
      description="API documentation for the HNG Stage 0 Backend Task. This API returns user profile information and a random cat fact.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"), # Change to your email
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # SWAGGER/DOCUMENTATION URLS
    # This path makes the Swagger UI available at the root of your site
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # These are optional but good to have for different documentation formats
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # YOUR API URLS
    # We are placing your API endpoint under the `/api/` namespace.
    # So, your /me endpoint will now be at /api/me/
    path("", include("profile_api.urls")),
    
    # DJANGO ADMIN URL
    path('admin/', admin.site.urls),
]