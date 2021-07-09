"""Seed file to make sample data for cupcakes DB."""

from models import Cupcake, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add sample users
cupcake1 = Cupcake(flavor="chocolate", size="small", rating=4.7)
cupcake2 = Cupcake(flavor="vanilla", size="small", rating=3.9)
cupcake3 = Cupcake(flavor="strawberry", size="small", rating=5.0)

# Add new objects to session, so they'll persist
db.session.add(cupcake1)
db.session.add(cupcake2)
db.session.add(cupcake3)


# Commit--otherwise, this never gets saved!
db.session.commit()