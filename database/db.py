from os.path import dirname, join, abspath
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields, post_load
from marshmallow_enum import EnumField
from enum import Enum


db = SQLAlchemy()
ma = Marshmallow()


class Companies(Enum):
    Panasonic = 0
    Bosh = 1
    Philips = 2
    Samsung = 3


class Technique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    manufactory_company = db.Column(db.Enum(Companies))
    year_of_manufacture = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    input_voltage = db.Column(db.Float, nullable=False)
    watts = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0):
        self.name = name
        self.model = model
        self.manufactory_company = manufactory_company
        self.year_of_manufacture = year_of_manufacture
        self.price = price
        self.input_voltage = input_voltage
        self.watts = watts

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n"


class TechniqueSchema(ma.Schema):
    # зефірка валідація
    name = fields.Str(validate=validate.Length(min=1, max=32))
    model = fields.Str(validate=validate.Length(min=1, max=20))
    manufactory_company = EnumField(Companies)
    year_of_manufacture = fields.Int(validate=validate.Range(min=1900, max=9999))
    price = fields.Float(validate=validate.Range(min=0.0, max=9999.999))
    input_voltage = fields.Float(validate=validate.Range(min=0.0, max=340.0))
    watts = fields.Int(validate=validate.Range(min=0, max=9999))

    # піздец важлива хрень десиріалізація з зефірки в пітон
    @post_load
    def make_technique(self, data, **kwargs):
        return Technique(**data)


technique_schema = TechniqueSchema()
techniques_schema = TechniqueSchema(many=True)


def create_db(app):
    try:
        db.create_all(app=app)
    except Exception as e:
        print(e)
        print("CANNOT CONNECT TO DB(CHECK config.py SQLALCHEMY_DATABASE_URI IF THIS FIELD IS OK) CREATING SQLITE DB")
        dbdir = join(dirname(dirname(abspath(__file__))), "database")
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(dbdir, 'db.sqlite')
        db.create_all(app=app)
