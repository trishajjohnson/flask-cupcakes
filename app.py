"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

# db.drop_all()
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """Renders homepage, base.html template."""
    cupcakes = Cupcake.query.all()

    return render_template("base.html", cupcakes=cupcakes)


@app.route("/api/cupcakes")
def list_cupcakes():
    
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Returns single cupcake JSON."""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """Creates new Cupcake instance."""

    flavor=request.json["flavor"]
    size=request.json["size"]
    rating=request.json["rating"]
    image=request.json.get("image", None)

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Updates single cupcake and returns JSON object."""

    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.query(Cupcake).filter_by(id=id).update(request.json)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())



@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """"Deletes cupcake."""

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=id)