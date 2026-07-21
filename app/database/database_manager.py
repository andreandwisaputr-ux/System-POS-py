"""
File    : database_manager.py
Project : SMART POS
Author  : Andrean Dwi
Description:
Mengelola koneksi database SQLite untuk seluruh aplikasi.
"""

import sqlite3
from pathlib import Path
from typing import Optional


class DatabaseManager:
    """Mengelola koneksi ke database SQLite."""

    def __init__(self, db_name: str = "smart_pos.db") -> None:

        project_root = Path(__file__).resolve().parents[2]
        self.db_path = project_root / db_name

        self._connection: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        """Membuka koneksi jika belum ada."""

        if self._connection is None:

            self._connection = sqlite3.connect(self.db_path)

            self._connection.row_factory = sqlite3.Row

        return self._connection

    def close(self) -> None:
        """Menutup koneksi database."""

        if self._connection is not None:

            self._connection.close()

            self._connection = None