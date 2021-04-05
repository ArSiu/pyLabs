from flask import Flask, request, jsonify
from database import Technique, technique_schema, techniques_schema, db, ma
from os.path import dirname, join, abspath


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:111@localhost/tech'


db.init_app(app)
ma.init_app(app)


# endpoint to create new technique
@app.route("/technique", methods=["POST"])
def add_technique():
    name = request.json["name"]
    model = request.json["model"]
    manufactory_company = request.json["manufactory_company"]
    year_of_manufacture = request.json["year_of_manufacture"]
    price = request.json["price"]
    input_voltage = request.json["input_voltage"]
    watts = request.json["watts"]

    technique = Technique(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts)

    db.session.add(technique)
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
    return technique_schema.jsonify(technique)


# endpoint to update technique
@app.route("/technique/<id>", methods=["PUT"])
def technique_update(id):
    technique = Technique.query.get(id)
    name = request.json["name"]
    model = request.json["model"]
    manufactory_company = request.json["manufactory_company"]
    year_of_manufacture = request.json["year_of_manufacture"]
    price = request.json["price"]
    input_voltage = request.json["input_voltage"]
    watts = request.json["watts"]

    technique.name = name
    technique.model = model
    technique.manufactory_company = manufactory_company
    technique.year_of_manufacture = year_of_manufacture
    technique.price = price
    technique.input_voltage = input_voltage
    technique.watts = watts

    db.session.commit()
    return technique_schema.jsonify(technique)


# endpoint to delete technique
@app.route("/technique/<id>", methods=["DELETE"])
def technique_delete(id):
    technique = Technique.query.get(id)
    db.session.delete(technique)
    db.session.commit()

    return technique_schema.jsonify(technique)


if __name__ == '__main__':
    try:
        db.create_all(app=app)
    except Exception as e:
        print(e)
        dbdir = join(dirname(dirname(abspath(__file__))), "database")
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(dbdir, 'db.sqlite')
        db.create_all(app=app)

    app.run(debug=True)
