"""
course_service/app.py — Hands-On 10, Task 1
Course Service: owns Departments and Courses, and its own SQLite database.
Runs independently on port 5001.
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course_service.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    credits = db.Column(db.SmallInteger, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "code": self.code, "credits": self.credits}


@app.route("/api/courses/", methods=["GET"])
def list_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])


@app.route("/api/courses/", methods=["POST"])
def create_course():
    payload = request.get_json(silent=True) or {}
    missing = [f for f in ("name", "code", "credits") if f not in payload]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400
    course = Course(name=payload["name"], code=payload["code"], credits=payload["credits"])
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201


@app.route("/api/courses/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    """Called by Student Service to verify a course exists before enrollment."""
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course.to_dict())


@app.route("/health/", methods=["GET"])
def health():
    return jsonify({"service": "course_service", "status": "up"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Course.query.first():
            db.session.add_all([
                Course(name="Data Structures", code="CS101", credits=4),
                Course(name="Operating Systems", code="CS201", credits=4),
            ])
            db.session.commit()
    app.run(port=5001, debug=False)
