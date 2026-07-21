from app.core.database import engine
from app.models.base import Base

# Import semua model
import app.models

Base.metadata.create_all(bind=engine)

print("Database berhasil dibuat.")