from typing import Generator, Any
from python_files.schamas_and_models.postgres_db_model import SessionLocal


def get_db() -> Generator[Any, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()