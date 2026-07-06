"""
courses/views.py — carried over from Hands-On 1, kept for continuity.
"""
from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("Course Management API is running")
