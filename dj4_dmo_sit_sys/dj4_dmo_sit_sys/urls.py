"""dj4_dmo_sit_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app_sin_bau_api import views as app_sin_bau_api_views

from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app_sin_bau_api/", include("app_sin_bau_api.urls")),
]

# swagger 視圖
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version="v1",
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)


# swagger 與 drf urls
urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

urlpatterns += [
    # re_path("static/(?P<path>.*)", serve, {"document_root": settings.STATIC_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
]
