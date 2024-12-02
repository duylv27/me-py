from sqlalchemy import Integer
from sqlalchemy.exc import SQLAlchemyError

from app.src.model.model import Person
from app.src.service import data_gen

class QueryService:

    def __init__(self):
        from db import engine
        self.engine = engine.engine
        self.session = engine.session
        self.data_gen = data_gen

    def get_session(self):
        return self.session

    def create(self):
        try:
            admin, regular = self.data_gen.create_user_objects()
            self.session.bulk_save_objects([admin, regular])
            self.session.commit()
        except Exception as e:
            print(f"Creating User got error {e}")

    def find_by_id(self, id: Integer) -> Person:
        try:
            print("Fetching...")
            selected_person = self.session.query(Person).filter(Person.id == id).first()
            return selected_person
        except SQLAlchemyError as e:
            print(f"SQLAlchemyError while fetching records: {e}")
        except Exception as e:
            print(f"Unexpected error while fetching records: {e}")

query_service = QueryService()
person = query_service.find_by_id(1)
print(person.id)
print(person.name)