"""
courses/urls.py — Hands-On 3, Task 2
Uses a DefaultRouter to auto-generate all CRUD URL patterns for each ViewSet.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("courses", views.CourseViewSet, basename="course")
router.register("students", views.StudentViewSet, basename="student")
router.register("enrollments", views.EnrollmentViewSet, basename="enrollment")
router.register("departments", views.DepartmentViewSet, basename="department")

urlpatterns = [
    path("hello/", views.hello_view, name="hello"),
    path("", include(router.urls)),
]
