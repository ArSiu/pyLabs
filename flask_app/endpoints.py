from flask import request, jsonify, abort
from marshmallow import ValidationError
from database import Technique, technique_schema, techniques_schema, db
from .app import app


# endpoint to create new technique
@app.route("/technique", methods=["POST"])
def add_technique():
    try:
        technique = technique_schema.load(request.json)
        db.session.add(technique)
    except ValidationError as err:
        abort(400, err)
    db.session.commit()

    return jsonify(request.json)


# endpoint to show all techniques
@app.route("/technique", methods=["GET"])
def get_techniques():
    all_techniques = Technique.query.all()
    result = techniques_schema.dump(all_techniques)
    return jsonify(result)


# endpoint to get technique detail by id
@app.route("/technique/<id>", methods=["GET"])
def technique_detail(id):
    technique = Technique.query.get(id)
    if technique is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)

    return technique_schema.jsonify(technique)


# endpoint to update technique
@app.route("/technique/<id>", methods=["PUT"])
def technique_update(id):
    technique = Technique.query.get(id)
    if not technique:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    try:
        technique = technique_schema.load(request.json)
        db.session.add(technique)
    except ValidationError as err:
        abort(400, err)
    db.session.commit()
    return technique_schema.jsonify(technique)


# endpoint to delete technique
@app.route("/technique/<id>", methods=["DELETE"])
def technique_delete(id):
    technique = Technique.query.get(id)
    if technique is None:
        response = jsonify({
            'status': 404,
            'description': "id not found"
        })
        abort(404, response)
    db.session.delete(technique)
    db.session.commit()
    return technique_schema.jsonify(technique)
