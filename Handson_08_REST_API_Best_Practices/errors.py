"""
errors.py — Hands-On 8, Task 2, Step 85
Standardised error response format + a shared exception handler.

Format:
{"error": {"code": "NOT_FOUND", "message": "...", "field": null}}
"""
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


def error_body(code: str, message: str, field: str | None = None):
    return {"error": {"code": code, "message": message, "field": field}}


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    code_map = {404: "NOT_FOUND", 400: "BAD_REQUEST", 401: "UNAUTHORIZED", 409: "CONFLICT"}
    code = code_map.get(exc.status_code, "ERROR")
    return JSONResponse(status_code=exc.status_code, content=error_body(code, str(exc.detail)))


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first = exc.errors()[0] if exc.errors() else {}
    field = ".".join(str(x) for x in first.get("loc", [])) if first else None
    return JSONResponse(
        status_code=422,
        content=error_body("VALIDATION_ERROR", "Request failed schema validation", field),
    )
