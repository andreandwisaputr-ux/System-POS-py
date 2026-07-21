from pathlib import Path

# Folder utama project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Folder database
DATABASE_DIR = BASE_DIR / "database"

# Jika folder database belum ada, buat otomatis
DATABASE_DIR.mkdir(exist_ok=True)

# Lokasi file SQLite
DATABASE_PATH = DATABASE_DIR / "smart_pos.db"

# SQLAlchemy Connection URL
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"