"""
notes.py — Hands-On 1, Task 1
Web Framework Foundations: Request-Response Cycle, Middleware, WSGI vs ASGI, MVC -> MVT

------------------------------------------------------------------------------
1. THE JOURNEY OF A GET /api/courses/ REQUEST
------------------------------------------------------------------------------
1. Browser/client sends an HTTP GET request to http://127.0.0.1:8000/api/courses/
2. The request first hits the WSGI/ASGI server (e.g. Django's dev server, or
   Gunicorn/Uvicorn in production), which hands it to Django's core handler.
3. Django's core wraps the raw request into an HttpRequest object and passes it
   through the MIDDLEWARE stack (each middleware can inspect/modify the request
   on the way in, and the response on the way out).
4. The URL ROUTER (coursemanager/urls.py -> courses/urls.py) matches the path
   '/api/courses/' against urlpatterns and resolves it to a VIEW function/class.
5. The VIEW executes business logic. If data is needed, it talks to a MODEL,
   which uses the Django ORM to build and execute a SQL query against the
   database (e.g. SELECT * FROM courses_course).
6. The MODEL returns Python objects (QuerySet) back to the VIEW.
7. The VIEW serializes/renders this data (in Hands-On 1 as plain text, later
   hands-ons as JSON via DRF serializers) and returns an HttpResponse.
8. The HttpResponse passes back OUT through the middleware stack (in reverse
   order), where response headers/cookies can be added.
9. The WSGI/ASGI server sends the final HTTP response back to the client.

    Client -> WSGI/ASGI Server -> Middleware (in) -> URL Router -> View
           -> Model (DB query) -> View -> Middleware (out) -> Client

------------------------------------------------------------------------------
2. MIDDLEWARE
------------------------------------------------------------------------------
Middleware sits BETWEEN the web server and the view, forming a chain that
every request/response passes through. Each middleware class can:
  - Process the request before it reaches the view (e.g. auth, security checks)
  - Process the response before it leaves Django (e.g. add headers, compress)

Two built-in Django middleware classes:
  - django.middleware.security.SecurityMiddleware:
      Adds security-related HTTP headers (HSTS, X-Content-Type-Options,
      SSL redirect enforcement) to protect against common web attacks.
  - django.contrib.sessions.middleware.SessionMiddleware:
      Enables session support by associating a session with each request via
      a cookie, allowing per-user state (e.g. login) to persist across requests.
  - django.middleware.csrf.CsrfViewMiddleware:
      Protects against Cross-Site Request Forgery by validating a CSRF token
      on unsafe HTTP methods (POST/PUT/DELETE).
  - django.contrib.auth.middleware.AuthenticationMiddleware:
      Attaches the currently logged-in user (request.user) to every request.

------------------------------------------------------------------------------
3. WSGI vs ASGI
------------------------------------------------------------------------------
WSGI (Web Server Gateway Interface):
  - The traditional, SYNCHRONOUS Python interface between web servers and
    Python web apps. One request is handled per worker thread/process at a
    time; it blocks while waiting on I/O (e.g. DB queries).

ASGI (Asynchronous Server Gateway Interface):
  - The modern, ASYNCHRONOUS successor to WSGI. Supports async/await, so a
    single worker can juggle many concurrent requests, WebSockets, and
    long-lived connections without blocking.

Django uses WSGI BY DEFAULT (see coursemanager/wsgi.py, used by
`manage.py runserver` and typical deployments with Gunicorn).

You would switch to ASGI (coursemanager/asgi.py, deployed with Uvicorn/
Daphne) when you need WebSockets, HTTP/2 server push, long-polling, or want
to use `async def` views for high-concurrency I/O-bound workloads.

------------------------------------------------------------------------------
4. MVC PATTERN -> DJANGO'S MVT MAPPING
------------------------------------------------------------------------------
MVC (Model-View-Controller):
  - Model:      Data & business logic
  - View:       Presentation / what the user sees
  - Controller: Handles input, coordinates Model and View

Django's MVT (Model-View-Template):
  - Model:      SAME as MVC's Model — represents data & handles DB access
                 (courses/models.py)
  - View:       Plays the role of MVC's CONTROLLER — receives the request,
                 talks to the Model, decides what data to send back
                 (courses/views.py)
  - Template:   Plays the role of MVC's VIEW — the presentation layer that
                 renders HTML/JSON to the client (templates/*.html, or a
                 JSON response for APIs)

  MVC Controller  == Django View
  MVC View        == Django Template
  MVC Model       == Django Model
"""


"""
------------------------------------------------------------------------------
HANDS-ON 2 ADDENDUM — Models, ORM & Admin
------------------------------------------------------------------------------
- ForeignKey(Model, on_delete=models.CASCADE) means deleting the parent row
  also deletes all related child rows. on_delete=models.SET_NULL (used on
  Student.department) instead nulls out the FK, keeping the Student record.
- unique_together on Enrollment.Meta prevents a student from enrolling in the
  same course twice at the database level.
- Always run `makemigrations` after changing models, then `migrate` to apply.
  Never hand-edit generated migration files unless you fully understand the
  operations being changed.
"""
