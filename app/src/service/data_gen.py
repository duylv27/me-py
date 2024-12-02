from typing import Tuple

from app.src.model.model import Person

def create_user_objects() -> Tuple[Person, Person]:
    admin_user = Person(
        name="toddthebod"
    )
    regular_user = Person(
        name="obnoxioustroll69",
    )
    return admin_user, regular_user