"""Cupcake Application Models."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://cdn2.vectorstock.com/i/1000x1000/25/16/cupcake-graphic-design-template-isolated-vector-31282516.jpg"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake model."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   unique=True)
    flavor = db.Column(db.Text,
                     nullable=False)
    size = db.Column(db.Text,
                     nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    def serialize(self):
        """Turns Cupcake instance into jsonify-able dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

