"""
extensions.py — Hands-On 5, Task 1
Holds shared Flask extension instances (db) so they can be imported by both
app.py and courses/models.py without circular imports.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
