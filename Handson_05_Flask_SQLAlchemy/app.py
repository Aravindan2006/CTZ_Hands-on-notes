"""
app.py — Hands-On 5
Application factory wired up to Flask-SQLAlchemy + Flask-Migrate.
"""
from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"status": "error", "message": str(e.description) if hasattr(e, "description") else "Not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"status": "error", "message": "Internal server error"}), 500

    @app.route("/")
    def index():
        return jsonify({"message": "Flask + SQLAlchemy Course Management API is running"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
