"""
courses/routes.py — Hands-On 5, Task 2
Real database-backed CRUD routes using Flask-SQLAlchemy, replacing the
in-memory list used in Hands-On 4.
"""
from flask import Blueprint, request, jsonify
from extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")


def make_response_json(data, status_code=200):
    return jsonify({"status": "success", "data": data}), status_code


@courses_bp.route("/", methods=["GET"])
def list_courses():
    courses = db.session.execute(db.select(Course)).scalars().all()
    return make_response_json([c.to_dict() for c in courses])


@courses_bp.route("/", methods=["POST"])
def create_course():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"status": "error", "message": "Request body must be JSON"}), 400

    missing = [f for f in ("name", "code", "credits", "department_id") if f not in payload]
    if missing:
        return jsonify({"status": "error", "message": f"Missing required fields: {missing}"}), 400

    course = Course(
        name=payload["name"],
        code=payload["code"],
        credits=payload["credits"],
        department_id=payload["department_id"],
    )
    db.session.add(course)
    db.session.commit()
    return make_response_json(course.to_dict(), 201)


@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    course = db.get_or_404(Course, course_id, description="Course not found")
    return make_response_json(course.to_dict())


@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):
    course = db.get_or_404(Course, course_id, description="Course not found")
    payload = request.get_json(silent=True) or {}
    for field in ("name", "code", "credits", "department_id"):
        if field in payload:
            setattr(course, field, payload[field])
    db.session.commit()
    return make_response_json(course.to_dict())


@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    course = db.get_or_404(Course, course_id, description="Course not found")
    db.session.delete(course)
    db.session.commit()
    return make_response_json({"deleted": course_id})


@courses_bp.route("/<int:course_id>/students/", methods=["GET"])
def course_students(course_id):
    """Task 2, Step 56 — JOIN query returning students enrolled in this course."""
    db.get_or_404(Course, course_id, description="Course not found")
    enrollments = db.session.execute(
        db.select(Enrollment).where(Enrollment.course_id == course_id)
    ).scalars().all()
    students = [e.student.to_dict() for e in enrollments]
    return make_response_json(students)
