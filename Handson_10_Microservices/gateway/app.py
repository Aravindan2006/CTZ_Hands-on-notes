"""
gateway/app.py — Hands-On 10, Task 2
A minimal API Gateway that proxies requests to the correct downstream
microservice based on the URL prefix. Runs on port 5000.

/api/courses/*  -> Course Service  (http://127.0.0.1:5001)
/api/students/* -> Student Service (http://127.0.0.1:5002)

A production gateway would also handle auth, rate limiting, and SSL
termination — this simple proxy only demonstrates the routing concept.
"""
from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

SERVICES = {
    "courses": "http://127.0.0.1:5001",
    "students": "http://127.0.0.1:5002",
}


def proxy(target_base, path):
    url = f"{target_base}/{path}"
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers={k: v for k, v in request.headers if k.lower() != "host"},
            params=request.args,
            data=request.get_data(),
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Upstream service unavailable"}), 503

    excluded_headers = {"content-encoding", "transfer-encoding", "connection"}
    headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded_headers]
    return Response(resp.content, status=resp.status_code, headers=headers)


@app.route("/api/courses/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/api/courses/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def route_courses(path):
    return proxy(SERVICES["courses"] + "/api/courses", path)


@app.route("/api/students/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/api/students/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def route_students(path):
    return proxy(SERVICES["students"] + "/api/students", path)


@app.route("/health/", methods=["GET"])
def health():
    return jsonify({"service": "gateway", "status": "up"})


if __name__ == "__main__":
    app.run(port=5000, debug=False)
