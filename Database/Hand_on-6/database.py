"""
Hands-On 6 : Task 1 (Steps 76, 79) + Session management
Engine, connection pooling, and session factory for the ORM layer.
"""

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import config
from models import Base

# ---------------------------------------------------------------------
# 76. Engine -- QueuePool is SQLAlchemy's default pool implementation;
#     tuning it explicitly makes the pooling behaviour visible/auditable.
# ---------------------------------------------------------------------
engine = create_engine(
    config.sqlalchemy_url,
    echo=config.ECHO_SQL,
    pool_size=config.POOL_SIZE,
    max_overflow=config.MAX_OVERFLOW,
    pool_timeout=config.POOL_TIMEOUT,
    pool_recycle=config.POOL_RECYCLE,
    pool_pre_ping=True,  # verifies connections are alive before use
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


@contextmanager
def get_session():
    """
    Context-managed session: commits on success, rolls back on error,
    always closes. Usage:
        with get_session() as session:
            session.add(obj)
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


# ---------------------------------------------------------------------
# 79. Create all tables (run this file directly to bootstrap the schema
#     into a fresh database, e.g. college_db_orm)
# ---------------------------------------------------------------------
def init_db():
    Base.metadata.create_all(bind=engine)
    print(f"All tables created in database: {config.DB_NAME}")


if __name__ == "__main__":
    init_db()
