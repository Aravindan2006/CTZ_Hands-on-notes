"""
courses/views.py — Hands-On 1, Task 2

Simple function-based view demonstrating the request-response cycle.
"""
from django.http import HttpResponse


def hello_view(request):
    """
    Handles GET /api/hello/
    Returns a plain-text response confirming the API is running.
    """
    return HttpResponse("Course Management API is running")
