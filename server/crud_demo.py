from app import app
from models import db, Pet

with app.app_context():
    db.create_all()

    # CREATE
    pet = Pet(name="Buddy", species="Dog")
    db.session.add(pet)
    db.session.commit()
    print("Created:", pet)

    # READ
    print("All pets:", Pet.query.all())
    print("By id:", db.session.get(Pet, pet.id))
    print("Dogs:", Pet.query.filter_by(species="Dog").all())

    # UPDATE
    pet.name = "Max"
    db.session.commit()
    print("Updated:", db.session.get(Pet, pet.id))

    # DELETE
    db.session.delete(pet)
    db.session.commit()
    print("After delete:", Pet.query.all())
