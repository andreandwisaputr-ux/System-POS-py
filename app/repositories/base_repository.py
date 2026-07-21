"""
File    : base_repository.py
Project : SMART POS
Author  : Kousetsu

Description:
Base class untuk seluruh repository.
Menyediakan akses ke DatabaseManager
dan helper yang akan digunakan bersama.
"""

from app.database.database_manager import DatabaseManager


class BaseRepository:

    def __init__(self, db: DatabaseManager):

        self.db = db

    @property
    def connection(self):
        """Mengembalikan objek koneksi SQLite."""

        return self.db.connect()

    @property
    def cursor(self):
        """Shortcut untuk mendapatkan cursor."""

        return self.connection.cursor()

    def commit(self) -> None:
        """Menyimpan perubahan ke database."""

        self.connection.commit()

    def rollback(self) -> None:
        """Membatalkan transaksi jika terjadi error."""

        self.connection.rollback()