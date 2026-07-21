from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

# Engine SQLite
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# Session Factory
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)