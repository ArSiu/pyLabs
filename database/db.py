from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
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
    manufactory_company = db.Column(db.Enum(Companies), nullable=False)
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
    class Meta:
        fields = ('name', 'model', ' manufactory_company', 'year_of_manufacture', 'price', 'input_voltage',
                  'watts')


technique_schema = TechniqueSchema()
techniques_schema = TechniqueSchema(many=True)
