"""
courses/urls.py — App-level URL configuration for the 'courses' app.
Kept separate from the project urls.py and included via include() to
keep URL configuration modular (best practice for multi-app projects).
"""
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_view, name="hello"),
]
