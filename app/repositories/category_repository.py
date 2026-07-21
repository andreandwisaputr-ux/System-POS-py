from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.category import Category


class CategoryRepository:

    def get_all(self):

        with SessionLocal() as session:

            stmt = select(Category).order_by(Category.name)

            return session.scalars(stmt).all()

    def create(self, name):

        with SessionLocal() as session:

            category = Category(name=name)

            session.add(category)

            session.commit()

            session.refresh(category)

            return category