"""
app.py — Hands-On 4, Task 1
Entry point using the Flask application factory pattern, which avoids
circular imports and makes the app easily testable.
"""
from flask import Flask, jsonify
from config import Config
from courses.routes import courses_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(courses_bp)

    # --- Task 2, Step 45 — JSON error handlers (APIs should never return HTML) ---
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"status": "error", "message": "Resource not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"status": "error", "message": "Internal server error"}), 500

    @app.route("/")
    def index():
        return jsonify({"message": "Flask Course Management API is running"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
