"""
student_service/app.py — Hands-On 10, Task 1 & 2
Student Service: owns Students and Enrollments, and its own SQLite database.
Runs independently on port 5002.

For enrollment, it must verify the course exists by calling Course Service's
GET /api/courses/{id}/ over HTTP (inter-service communication) — it never
queries Course Service's database directly (Task 1, Step 96 principle:
each service owns its data).
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student_service.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

COURSE_SERVICE_URL = "http://127.0.0.1:5001"


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email}


class Enrollment(db.Model):
    __tablename__ = "enrollments"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    course_id = db.Column(db.Integer, nullable=False)  # owned by Course Service, not a local FK

    def to_dict(self):
        return {"id": self.id, "student_id": self.student_id, "course_id": self.course_id}


@app.route("/api/students/", methods=["GET"])
def list_students():
    return jsonify([s.to_dict() for s in Student.query.all()])


@app.route("/api/students/", methods=["POST"])
def create_student():
    payload = request.get_json(silent=True) or {}
    missing = [f for f in ("first_name", "last_name", "email") if f not in payload]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400
    student = Student(first_name=payload["first_name"], last_name=payload["last_name"], email=payload["email"])
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201


@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def enroll(student_id):
    """
    Task 2, Step 100-101 — verifies the course exists via a synchronous HTTP
    call to Course Service, and gracefully handles Course Service being down.
    """
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    payload = request.get_json(silent=True) or {}
    course_id = payload.get("course_id")
    if course_id is None:
        return jsonify({"error": "course_id is required"}), 400

    try:
        resp = requests.get(f"{COURSE_SERVICE_URL}/api/courses/{course_id}/", timeout=3)
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Course Service is unavailable"}), 503

    if resp.status_code == 404:
        return jsonify({"error": f"Course {course_id} does not exist"}), 404
    if resp.status_code != 200:
        return jsonify({"error": "Unexpected error from Course Service"}), 502

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    return jsonify(enrollment.to_dict()), 201


@app.route("/health/", methods=["GET"])
def health():
    return jsonify({"service": "student_service", "status": "up"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Student.query.first():
            db.session.add_all([
                Student(first_name="Asha", last_name="Menon", email="asha@college.edu"),
                Student(first_name="Ravi", last_name="Kumar", email="ravi@college.edu"),
            ])
            db.session.commit()
    app.run(port=5002, debug=False)
