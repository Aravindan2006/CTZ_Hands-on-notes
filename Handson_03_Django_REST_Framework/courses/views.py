"""
courses/views.py — Hands-On 3
Task 1 keeps CourseListView/CourseDetailView (APIView) as a learning step.
Task 2 refactors to ViewSets, which is what's actually wired up in urls.py.
"""
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Department, Course, Student, Enrollment
from .serializers import (
    DepartmentSerializer,
    CourseSerializer,
    StudentSerializer,
    EnrollmentSerializer,
)


def hello_view(request):
    """Carried over from Hands-On 1."""
    return HttpResponse("Course Management API is running")


# ---------------------------------------------------------------------------
# Task 1 — APIView based views (kept for reference; not wired into urls.py,
# superseded by the ViewSets below which do the same job in fewer lines).
# ---------------------------------------------------------------------------
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(CourseSerializer(course).data)

    def put(self, request, pk):
        course = self.get_object(pk)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        if course is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# Task 2 — ViewSets + Router (this is what urls.py actually exposes)
# ---------------------------------------------------------------------------
class CourseViewSet(viewsets.ModelViewSet):
    """Full CRUD for Course, plus a custom /students/ action."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        """GET /api/courses/{id}/students/ — students enrolled in this course."""
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course).select_related("student")
        students = [e.student for e in enrollments]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
