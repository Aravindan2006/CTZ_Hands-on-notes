# Hands-On 10 — Microservices Architecture: Concepts & Decomposition

## Project Description
Decomposes the monolithic Course Management API into two independent Flask
microservices — **Course Service** and **Student Service** — each with its
own SQLite database, plus a minimal **API Gateway** that proxies requests to
the correct service. The Student Service calls the Course Service
synchronously over HTTP to verify a course exists before enrolling a
student, and gracefully returns `503` if the Course Service is unreachable.

## Service Decomposition

| Service            | Responsibility                          | Endpoints it owns                              | Database it owns          |
|---------------------|--------------------------------------------|----------------------------------------------------|------------------------------|
| **Course Service**   | Course CRUD                                | `/api/courses/`, `/api/courses/{id}/`               | `course_service.db`           |
| **Student Service**  | Student CRUD, Enrollment                   | `/api/students/`, `/api/students/{id}/enroll`       | `student_service.db`          |
| **API Gateway**       | Routes external traffic to the right service | `/api/courses/*` → Course Service, `/api/students/*` → Student Service | none (stateless proxy) |
| *(Conceptual, not implemented)* Auth Service | registration, login, token validation | `/api/v1/auth/*` (see Hands-On 9) | own user DB |
| *(Conceptual, not implemented)* Notification Service | email confirmations | internal only | none |

**Key principle**: each service owns its own data — no service queries
another service's database directly.

## Technologies
- Python 3.10+, Flask, Flask-SQLAlchemy, `requests` (inter-service HTTP calls), SQLite

## Installation
```bash
cd Handson_10_Microservices
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Run Instructions
Run each service in its own terminal (independent processes, independent DBs):
```bash
# Terminal 1
cd course_service && python app.py     # http://127.0.0.1:5001

# Terminal 2
cd student_service && python app.py    # http://127.0.0.1:5002

# Terminal 3
cd gateway && python app.py            # http://127.0.0.1:5000
```

Test the full flow through the gateway:
```bash
curl -X POST http://127.0.0.1:5000/api/students/1/enroll \
  -H "Content-Type: application/json" -d '{"course_id": 1}'
```
Stop Course Service and repeat the request — you'll get a `503 Service Unavailable`.

## Folder Structure
```
Handson_10_Microservices/
├── course_service/app.py     # port 5001, own DB
├── student_service/app.py    # port 5002, own DB, calls Course Service
├── gateway/app.py            # port 5000, proxies to both services
├── postman/
├── screenshots/
├── requirements.txt
└── .gitignore
```

## Features
- Two fully independent Flask microservices, each with its own SQLite DB
- Synchronous inter-service HTTP call (Student → Course Service) using `requests`
- Graceful `503` handling when a downstream service is unavailable
- A minimal API Gateway demonstrating the routing pattern

## API Endpoints
| Method | Endpoint (via Gateway, port 5000)   | Forwards to      | Description                  |
|--------|-----------------------------------------|--------------------|---------------------------------|
| GET    | `/api/courses/`                        | Course Service      | List courses                    |
| POST   | `/api/courses/`                         | Course Service      | Create a course                 |
| GET    | `/api/students/`                       | Student Service      | List students                   |
| POST   | `/api/students/`                        | Student Service      | Create a student                |
| POST   | `/api/students/{id}/enroll`            | Student Service (→ Course Service) | Enroll, verifying the course first |

## Screenshots
See `screenshots/` folder.

## Synchronous vs Asynchronous Inter-Service Communication (Task 2, Step 104)
**Synchronous (HTTP, used here)**: simple to implement and reason about, but
creates tight coupling — if Course Service is down, enrollment fails
immediately (as demonstrated by the `503` above).

**Asynchronous (message queue, e.g. RabbitMQ/Kafka)**: the Student Service
would publish an "EnrollmentRequested" event and continue immediately; a
consumer would validate and confirm later. This decouples the services and
improves availability, at the cost of eventual consistency and added
operational complexity (you now have to manage the queue itself). Use a
message queue when services can tolerate eventual consistency and you need
resilience to downstream outages or bursty traffic; use direct HTTP calls
(as here) when you need an immediate, synchronous answer such as validating
a foreign resource before completing a request.

## Learning Outcomes
- Identified natural service boundaries in a monolithic API
- Built two independent microservices, each owning its own data
- Implemented synchronous inter-service communication with `requests`
- Handled downstream service failure gracefully with `503`
- Built a minimal API Gateway and understood what a production gateway adds
  (auth, rate limiting, SSL termination)
