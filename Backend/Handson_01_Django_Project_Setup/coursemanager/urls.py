# urls.py — see module docstring below for role.
"""
coursemanager/urls.py — Root URL configuration for the project.
Role: maps top-level URL prefixes to each app's own urls.py using include(),
so every app owns its own URL namespace.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),          # Django admin site
    path("api/", include("courses.urls")),    # Delegates /api/* to courses app
]
